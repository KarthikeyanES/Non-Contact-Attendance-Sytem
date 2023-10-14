# # import os
# # from http.server import HTTPServer, CGIHTTPRequestHandler
# #
# # # Make sure the server is created at current directory
# # os.chdir('Wifi.localIP()')
# # # Create server object listening the port 80
# # server_object = HTTPServer(server_address=('192.168.137.38', 80), RequestHandlerClass=CGIHTTPRequestHandler)
# # # Start the web server
# # server_object.serve_forever()
# from cgitb import text
#
# from _dlib_pybind11.image_dataset_metadata import box
# from pandas.io.formats.style import color
#
# import serial  # Serial imported for Serial communication
# import time  # Required to use delay functions
#
# ArduinoSerial = serial.Serial('com18', 9600)  # Create Serial port object called arduinoSerialData
# time.sleep(2)  # wait for 2 secounds for the communication to get established
#
# obj = box(pos=(-5, 0, 0), size=(0.1, 4, 4), color=color.white)
# wallL = box(pos=(-1, 0, 0), size=(0.2, 12, 12), color=color.cyan)
# text(text='US sensor', axis=(0, 1, 0), pos=(-2, -6, 0), depth=-0.3, color=color.cyan)
#
# t = 0
#
#
# def rate(param):
#     pass
#
#
# while 1:
#     rate(100)
#     t = int(ArduinoSerial.readline())  # read the serial data and print it as line
#     t = t * 0.05
#     obj.pos.x = t
#     print(t)
#
