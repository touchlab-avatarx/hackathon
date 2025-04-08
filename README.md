# Hackathon
Example code to read touchlab sensors

1: Install pyserial - pip install pyserial
2: Plug in your USB cable which is connected to the board and the touchlab sensor
    NB. MAke sure to match the dot on the sensor connector to the dot on the board to ensure the
    pins are connected correctly
    If the sensor is not connected to the correct pins you will see no change in the sensor output
3: Run the readout_string.py file and pass it the corresponding port

    Windows example: python3 readout_string.py COM3
    Linux example:   python3 readout_string.py /dev/ttyACM0

4: Each sensor has 4 separate elements, each of which will return a int value