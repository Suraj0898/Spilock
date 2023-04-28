# Adding the required libraries
from utils import i2c_lcd_driver
from utils import rfid
import RPi.GPIO as GPIO
from mfrc522 import SimpleMFRC522
from time import sleep


def scan():
    # Adding the Buzzer Pin
    buzzer = 19

    GPIO.setmode(GPIO.BCM)
    GPIO.setwarnings(False)
    GPIO.setup(buzzer, GPIO.OUT)

    # Add a LCD object
    mylcd = i2c_lcd_driver.lcd()

    # Add a RFID module object
    scan = SimpleMFRC522()

    try:
        print("Place your Key Card to Scan")
        mylcd.lcd_display_string("Place your Tag", 1)
        scan.write("Tag ID")
        id, Tag = scan.read()
        my_rfid = rfid()
        my_rfid.set_rfid(str(id))
        print("Your Tag ID is: " + str(id))
        mylcd.lcd_clear()
        mylcd.lcd_display_string("Tag ID", 1, 5)
        mylcd.lcd_display_string(str(id), 2, 1)

        GPIO.output(buzzer, GPIO.HIGH)
        sleep(0.5)
        GPIO.output(buzzer, GPIO.LOW)

    finally:
        GPIO.cleanup()

    return my_rfid
