#!/usr/bin/env python3
# Copyright (c) 2025 Touchlab Limited. All Rights Reserved
# Unauthorized copying or modifications of this file, via any medium is strictly prohibited.

import serial
import signal
import sys

is_running = True

def sigint_handler(*args):
    global is_running
    is_running = False

def read(ser : serial.Serial):
    max_taxels = 512

    buffer = ser.readline().decode('utf8')
    strings = buffer.split(',')
    num_taxels = len(strings)
    try:
        if num_taxels > 0 and num_taxels < max_taxels: # Make sure we didn't read rubbish
            # Read and parse taxels
            val = [0] * num_taxels
            for i in range(num_taxels):
                # print(strings[i])
                val[i] = int(strings[i])
            return val
        else:
            return None
    except ValueError:
        print(f"Error parsing values: {strings}")
        return None

def main():
    global is_running
    signal.signal(signal.SIGINT, sigint_handler) # Handle ctrl+c in terminal
    try:
        with serial.Serial(sys.argv[-1], 115200, timeout=0.5) as ser:
            ser.read_all()
            while is_running:
                values = read(ser)
                if values is None:
                    continue
                else:
                    print(f"{values}".replace(" ", "\t"))
    except serial.serialutil.SerialException:
        print('Serial port not available')

if __name__ == '__main__':
    main()
