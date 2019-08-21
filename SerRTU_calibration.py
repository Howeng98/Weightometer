from pymodbus.client.sync import ModbusSerialClient as ModbusClient

scale = ModbusClient(method='rtu', port='/dev/ttyUSB0', parity='N', baudrate=9600, bytesize=8, stopbits=2, timeout=1)
connection = scale.connect()
print(connection)


'''
step001 去皮歸零 start:
'''


InitStart_write = scale.write_registers(1100, 1, unit=16) #去皮歸零 (start addr , count, deviceID)
b = scale.read_input_registers(0, 10, unit=16)
print('weight - channel1 in U16 :', b.registers)




'''
去皮歸零 end＊＊
'''



'''
tep002 秤重 start:
'''

weight_read = scale.read_input_registers(0,10,unit=16)
print('channel1 in U16 :' , weight_read.registers)
print(type(weight_read.registers[0]))

'''
秤重 end＊＊
'''



'''
step003 校準模式 start:
'''
'''
#modeStart_write = scale.write_registers(1009, 170, unit=16)
modeStart_read = scale.read_holding_registers(1009, 3, unit=16) #Test GitHub
print(modeStart_read.registers)
'''
'''
校準模式 end:拔掉電源＊＊
'''

'''
step004 量程校準 start:
'''

#read and write ADC1：重量較小
'''
valueADC_read = scale.read_input_registers(100, 2, unit=16)
print(valueADC_read.registers)
valueADC_write = scale.write_registers(301, valueADC_read.registers[1], unit=16) #read and write second index
'''
#debug
'''
valueADC_read2 = scale.read_holding_registers(300, 2, unit=16)
print(valueADC_read2.registers)
'''
#write ADC1對應的實際 weight

#valueWeight_write = scale.write_registers(303, 22, unit=16) 

#debug
'''
valueWeight_read = scale.read_holding_registers(302, 2, unit=16)
print(valueWeight_read.registers)
'''

#read and write ADC2：重量較大

'''
valueADC_read = scale.read_input_registers(100, 2, unit=16)
print(valueADC_read.registers)
valueADC_write = scale.write_registers(305, valueADC_read.registers[1], unit=16)
'''

#debug
'''
valueADC_read2 = scale.read_holding_registers(304, 2, unit=16)
print(valueADC_read2.registers)
'''

#write ADC2對應的實際 weight

#valueWeight_write = scale.write_registers(307, 2600, unit=16)

#debug
'''
valueWeight_read = scale.read_holding_registers(306, 2, unit=16)
print(valueWeight_read.registers)
'''
'''
量程校準 end:將ADC1,ADC1_weight ADC2,ADC2_weight寫入後,完成量程校準＊＊

'''

scale.close()

