# Simple GPS datalogging demonstration.
# This actually doesn't even use the GPS library and instead just reads raw
# NMEA sentences from the GPS unit and dumps them to a file on an SD card
# (recommended) or internal storage (be careful as only a few kilobytes to
# megabytes are available).  Before writing to internal storage you MUST
# carefully follow the steps in this guide to enable writes to the internal
# filesystem:
#  https://learn.adafruit.com/adafruit-ultimate-gps-featherwing/circuitpython-library

import os
from machine import UART
uart = UART(0, 9600, timeout=3000) # UART interface for GPS
LOG_FILE = '/gps.txt'  # Example for writing to internal path /gps.txt
#LOG_FILE = '/sd/gps.txt'     # Example for writing to SD card path /sd/gps.txt
LOG_MODE = 'ab' # 'a' for appending, 'w' for overwrite

# If writing to SD card customize and uncomment these lines to import the
# necessary library and initialize the SD card:
# import machine, sdcard, os
# sd = sdcard.SDCard(machine.Pin(16), machine.SPI(1))
# os.mount(sd, '/sd')

# Create a file for logging GPS data
with open(LOG_FILE, LOG_MODE) as outfile:
    while True:
        sentence = uart.readline()
        print(str(sentence, 'ascii').strip())
        outfile.write(sentence)
        outfile.flush()
