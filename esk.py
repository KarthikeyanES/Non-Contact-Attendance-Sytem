

import serial
import time


s = serial.Serial('COM6',9600)

s.timeout = 30246
rs= s.readline()
Rs=rs.decode()
print(Rs[0])
d=Rs[0]
print(d)

# d=not(rs)

# print(rs)
s.close()


























# import serial
# import time
# import curses
# import threading
# global uart
# uart = true
#
# screen = curses.initscr()
#
#
# row=0
# col=0
# screen.addstr(row,col,"Data: ")
# screen.refresh()
#
#
#
# def mys():
#     global uart
#     port = "COM6"
#     d = serial.erial(port, 9600, timeout=0)
#     while uart:
#         ud = d.readline()
#         ud_s = ud.decode('utf8')
#         #    print(ud_sensor)
#         # screen.addstr(row, 8, "      ")
#         screen.addstr(row, 8, ud_s)
#         screen.refresh()
#
# t1 = threading.Thread(target=mys)
# t1.daemon=True
# t1.start()
#
# while True:
#     key = screen.getkey()
#     if key == 'q':
#         uart = False
#         break
#
# # make sure the 'COM#' is set according the Windows Device Manager
# # import serial.tools.list_ports
# #
# # ports = serial.tools.list_ports.comports()
# # serialInst = serial.Serial()
# #
# # portsList = []
# #
# # for onePort in ports:
# #     portsList.append(str(onePort))
# #     print(str(onePort))
# #
# # val = input("Select Port: COM")
# #
# # for x in range(0,len(portsList)):
# #     if portsList[x].startswith("COM" + str(val)):
# #         portVar = "COM" + str(val)
# #         print(portVar)
# #
# # serialInst.baudrate = 9600
# # serialInst.port = portVar
# # serialInst.open()
# #
# # while True:
# # 	if serialInst.in_waiting:
# # 		packet = serialInst.readline()
# # 		print(packet.decode('utf').rstrip('\n'))