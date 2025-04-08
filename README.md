# Hackathon

### Example code to read touchlab triaxial sensors

1. Install pyserial - `pip install pyserial`
2. Plug in your USB cable which is connected to the board and the touchlab fabric sensor. Make sure to match the dot on the sensor connector to the dot on the board to ensure the pins are connected correctly. If the sensor is not connected to the correct pins you will see no change in the sensor output but the sensor will not get damaged.
3. Run the readout_triaxial.py file and pass it the port corresponding port:
   > Windows example: `python3 readout_triaxial.py COM3`
   > 
   > Linux example:   `python3 readout_triaxial.py /dev/ttyACM0`

4. Each sensor has 4 separate elements, each of which will return a float value

### Example code to read touchlab fabric sensors

1. Install pyserial - `pip install pyserial`
2. Plug in your USB cable which is connected to the board and the touchlab fabric sensor. Make sure to match the dot on the sensor connector to the dot on the board to ensure the pins are connected correctly. If the sensor is not connected to the correct pins you will see no change in the sensor output but the sensor will not get damaged.
3. Run the readout_fabric.py file and pass it the port corresponding port:
   > Windows example: `python3 readout_fabric.py COM3`
   > 
   > Linux example:   `python3 readout_fabric.py /dev/ttyACM0`

4. Each sensor has 5 separate elements, each of which will return a float value
