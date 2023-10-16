# Robotarium_hackathon
Example code to read touchlab fabric sensors

1: Install pyserial - pip install pyserial
2: Plug in your USB cable which is connected to the board and the touchlab fabric sensor
    If the sensor is not connected to the correct pins you will see no change in the sensor output
3: Run the touchlab_fabric_reader.py file and pass it the port corresponding port

    Windows example: python3 touchlab_fabric_reader.py COM3
    Linux example:   python3 touchlab_fabric_reader.py /dev/ttyACM0

4: Each sensor has 5 separate elements, each of which will return a float value