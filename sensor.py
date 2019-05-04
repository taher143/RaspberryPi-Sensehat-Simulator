#!/usr/bin/python
# COPYRIGHT
#     Copyright (c) 2016 by Cisco Systems, Inc.
#     All rights reserved.
#
# DESCRIPTION
#     Raspberry Sensorhat sensor operations.
#from sense_hat import SenseHat
#sense = SenseHat()
import time
import serial
import random
# #open serial port for arduino
# ser = serial.Serial('/dev/ttyACM0', 9600)
# line = ""

# #function to find substring
# def find_between( s, first, last ):
#     try:
#         start = s.index( first ) + len( first )
#         end = s.index( last, start )
#         return s[start:end]
#     except ValueError:
#         return ""

# #function to find substring occur last
# def find_between_r( s, first, last ):
#     try:
#         start = s.rindex( first ) + len( first )
#         end = s.rindex( last, start )
#         return s[start:end]
#     except ValueError:
#         return ""

# Round the data to two digit float
def get_data_rounded(raw_data):
    print(raw_data)	
    if type(raw_data) is dict:
        for key in raw_data:
            raw_data[key] = float("{0:.2f}".format(raw_data[key]))
    else:
        if type(raw_data) is float:
            raw_data = float("{0:.2f}".format(raw_data))
            print(raw_data)
    return raw_data

# Get the sensehat data, return None if the item requested is not available
def get_data(type):
    temp = random.randint(100,200)
    print temp
    return temp
    # return {
    #  'temperature':         get_data_rounded(25),
    #  'humidity':            get_data_rounded(50),
    #  'pressure':            get_data_rounded(40),
    #  'magnetometer':        get_data_rounded(4),
    #  'accelerometer':       get_data_rounded(90),
    #  'gyroscope':           get_data_rounded(90)
    #  # 'temperature':         get_data_rounded(sense.get_temperature),
    #  # 'humidity':            get_data_rounded(sense.get_humidity),
    #  # 'pressure':            get_data_rounded(sense.get_pressure),
    #  # 'magnetometer':        get_data_rounded(sense.get_compass_raw),
    #  # 'accelerometer':       get_data_rounded(sense.get_accelerometer),
    #  # 'gyroscope':           get_data_rounded(sense.get_gyroscope)
    #   }.get(type, 'None')()





# colours = {
#     'black': [0, 0, 0],
#     'white': [255, 255, 255],
#     'red': [255, 0, 0],
#     'green': [0, 255, 0],
#     'blue': [0, 0, 255],
#     'yellow': [255, 255, 0],
#     'magenta': [255, 0, 255],
#     'cyan': [0, 255, 255]}


# def colourNameToRgb(colour):
#      return colours.get(colour,[0, 0, 255])
