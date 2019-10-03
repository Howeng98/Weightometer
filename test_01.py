from pymodbus.client.sync import ModbusSerialClient as ModbusClient
import time
import logging

#logging.basicConfig()
#log = logging.getLogger()
#log.setLevel(logging.DEBUG)

scale = ModbusClient(method='rtu', port='/dev/ttyUSB0', parity='N', baudrate=9600, bytesize=8, stopbits=2, timeout=1)
connection = scale.connect()

while True:
    try:
        time.sleep(1)
        #InitStart_write = scale.write_registers(1100, 1, unit=16)  # 去皮歸零 (start addr , count, deviceID)
        b = scale.read_input_registers(100, 1, unit=16)
        print('The weight is :', b.registers)
    except Exception as e:
        print(e)

scale.close()
