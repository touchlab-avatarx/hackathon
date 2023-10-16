import serial
import signal
import sys
import time

is_running = True

def sigint_handler(*args):
    is_running = False

def main():
    try:
        signal.signal(signal.SIGINT, sigint_handler) # Handle ctrl+c in terminal
        print(f'Connecting to {sys.argv[-1]}')
        with serial.Serial(sys.argv[-1], 11500, timeout=1) as ser:
            ser.flush()
            while is_running:
                sensor_data = []
                data = ser.readline()[:-1]
                split = data.split(b',')

                for value in split:
                    sensor_data.append(float(value))

                print(sensor_data)
                time.sleep(0.001)
    except KeyboardInterrupt:
        pass

if __name__ == '__main__':
    main()