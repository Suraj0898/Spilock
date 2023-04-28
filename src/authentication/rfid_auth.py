# Include the library files
from src.actuator import relay_buzzer
from src.application.notification import http_post
from src.sensor.scan import scan
from utils import i2c_lcd_driver
import RPi.GPIO as GPIO
from mfrc522 import SimpleMFRC522
from time import sleep

# Include the buzzer pin
from utils.rfid import rfid

buzzer = 19

# Include the relay pin
relay = 26

# Enter your tag ID
my_rfid = rfid()
my_rfid = scan()
Tag_ID = my_rfid.get_tag()

door = True

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(buzzer, GPIO.OUT)
GPIO.setup(relay, GPIO.OUT)

# Create a object for the LCD
lcd = i2c_lcd_driver.lcd()

# Create a object for the RFID module
read = SimpleMFRC522()


def rfid_auth():
    lcd.lcd_display_string("Step 1: RFID Authentication", 1, 0)
    for a in range(0, 15):
        lcd.lcd_display_string(".", 2, a)
        sleep(0.1)

    while True:
        lcd.lcd_clear()
        print("Place your Key Card to Scan")
        lcd.lcd_display_string("Place your Tag", 1, 1)
        id, Tag = read.read()

        id = str(id)

        if id == Tag_ID:
            lcd.lcd_clear()
            print("Successful!")
            lcd.lcd_display_string("Successful", 1, 3)
            door = not door

            if door == True:
                print("Door is locked")
                lcd.lcd_display_string("Door is locked", 2, 1)
                relay_buzzer.door_locked(buzzer, relay)
                return False

            elif door == False:
                print("Correct Key")
                lcd.lcd_display_string("Correct Key", 2, 2)
                return True

        else:
            lcd.lcd_clear()
            print("Wrong Tap!")
            lcd.lcd_display_string("Wrong Tag!", 1, 3)
            relay_buzzer.wrong_tap(buzzer, relay)
            http_post()

    GPIO.cleanup()
