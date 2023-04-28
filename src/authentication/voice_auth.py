from src.actuator import relay_buzzer
from src.application.notification import http_post
from src.database.mongo import query_question, query_answer
from src.sensor.listen import listen
from utils import i2c_lcd_driver
import RPi.GPIO as GPIO
from mfrc522 import SimpleMFRC522
from time import sleep

from utils.microphone import microphone

buzzer = 19

# Include the relay pin
relay = 26

# Enter your tag ID
my_microphone = microphone()
my_microphone = listen()
mic_answer = my_microphone.get_response()

door = True

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(buzzer, GPIO.OUT)
GPIO.setup(relay, GPIO.OUT)

# Create a object for the LCD
lcd = i2c_lcd_driver.lcd()


def voice_auth():
    lcd.lcd_display_string("Voice Verification", 1, 0)
    for a in range(0, 15):
        lcd.lcd_display_string(".", 2, a)
        sleep(0.1)

    while True:
        lcd.lcd_clear()
        question = query_question()
        print(question)
        lcd.lcd_display_string(question, 1, 1)

        valid_answer = query_answer(question)

        if mic_answer == valid_answer:
            lcd.lcd_clear()
            print("Successful!")
            lcd.lcd_display_string("Successful", 1, 3)

            print("Door is open")
            lcd.lcd_display_string("Door is open", 2, 2)
            relay_buzzer.door_open(buzzer, relay)

        else:
            lcd.lcd_clear()
            print("Wrong Answer!")
            lcd.lcd_display_string("Wrong Answer!", 1, 3)
            relay_buzzer.wrong_tap(buzzer, relay)
            http_post()

    GPIO.cleanup()