# Spilock
### Project Overview:
Spilock is an IoT Embedded System design project which is a 2 factor authentication based door locking system. The system uses an RFID scanning module for the first authentication, and a personal question with voice response for the second authentication. The project is designed using Python programming language and the components used in the project include Raspberry Pi, MQTT, RFID module, LCD display, breadboard, MongoDB, buzzer, and relay module.

### Setup and Installation:
To install and set up the Spilock IoT project, follow the instructions below:

- Connect the Raspberry Pi to the breadboard and connect the RFID module, buzzer, relay module, and LCD display to the breadboard.
- Install the necessary libraries and packages such as Pymongo, MFRC522, Rpi.GPIO, etc. on the Raspberry Pi.
- Clone the project repository from the Github page and open the code in Python IDE such as PyCharm or Visual Studio Code.
- Open the "config.py" file and edit the settings such as database connection, MQTT broker, and GPIO pins to match your own configuration.
- Run the "main.py" file to start the application.

### Usage:
To use the Spilock IoT project, follow the instructions below:

- Scan the RFID card to initiate the first authentication.
- The LCD display will show the status of the RFID authentication.
- If the RFID authentication is successful, the system will prompt you to answer a personal question.
- Record your voice response and the system will compare it with the stored voice response.
- If the voice response authentication is successful, the system will unlock the door using the relay module and turn on the buzzer to signal successful authentication.
- If either authentication fails, the system will deny access and notify the user via the LCD display.

### Sensor and Actuator:
The sensors used in this project include an RFID module for card scanning, while the actuator used is a relay module to control the door lock.

## Conclusion:
Spilock is a reliable and secure 2-factor authentication based door locking system, designed to keep your property safe. The project can be further enhanced to include additional features such as facial recognition, motion detection, and remote access control.

# Contributors:
- Sonali Mondal (NUID: 002128542)
- Suraj Suhas (NUID: 002747142)
