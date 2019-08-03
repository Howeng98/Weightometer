import sys
from PyQt5 import QtWidgets,QtGui,QtCore
from PyQt5.QtWidgets import QDialog,QApplication,QPushButton,QMainWindow,QLabel
import SerRTU_calibration


def connect():
    try:
        SerRTU_calibration.start()
        label.setText("Connect Successful")
    except Exception as e:
        print(e)

def start():
    try:
        SerRTU_calibration.stepOne()
        label.setText("" + str(SerRTU_calibration.b.registers[0]))
    except Exception as e:
        print(e)

def stop():
    try:
        SerRTU_calibration.close()
    except Exception as e:
        print(e)
    QtCore.QCoreApplication.instance().quit()


class Mainwindow(QMainWindow):

    def __init__(self):
        QMainWindow.__init__(self)
        self.setWindowTitle("Gui window")
        self.setGeometry(50, 50, 1000, 600)
        self.buttonGenerate()
        self.labelGenerate()

    def buttonGenerate(self):
        """connect Button"""
        connectButton = QPushButton("Connect",self)
        connectButton.clicked.connect(connect)
        connectButton.resize(100, 50)
        connectButton.move(320,300)

        """start Button"""
        startButton = QPushButton("Start", self)
        startButton.clicked.connect(start)
        startButton.resize(100, 50)
        startButton.move(450, 300)

        """stop Button"""
        stopButton = QPushButton("Stop", self)
        stopButton.clicked.connect(stop)
        stopButton.resize(100, 50)
        stopButton.move(580, 300)

    def labelGenerate(self):
        global label
        label = QtWidgets.QLabel(self)
        label.setText("Welcome")
        label.resize(1000, 50)
        label.move(0, 200)
        label.setFont(QtGui.QFont("Sanserif", 30))
        label.setAlignment(QtCore.Qt.AlignCenter)


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    mainWindow = Mainwindow()
    mainWindow.show()
    sys.exit(app.exec_())

