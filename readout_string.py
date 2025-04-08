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

def read(ser : serial.Serial, header : list):
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

def vector(taxels:list):
    """Creates a 3D vector from the taxel values when  using a Touchlab triaxial sensor.

    Args:
        taxels (list): The four taxels of the sensor

    Returns:
        _type_: 3D force vector x, y, z
    """
    x = taxels[3] - taxels[1]
    y = taxels[2] - taxels[0]
    z = taxels[0]+ taxels[1] + taxels[2] +taxels[3]
    return x, y, z

def main():
    global is_running
    signal.signal(signal.SIGINT, sigint_handler) # Handle ctrl+c in terminal
    try:
        with serial.Serial(sys.argv[-1], 115200, timeout=0.5) as ser:
            ser.read_all()
            header = [b'\x00', b'\x00']
            while is_running:
                # Check for the header
                values = read(ser, header)
                if values is None:
                    continue
                else:
                    print(f"{values}".replace(" ", "\t"))
                    print(f"Vector {vector(values)}")
    except serial.serialutil.SerialException:
        print('Serial port not available')

if __name__ == '__main__':
    main()
