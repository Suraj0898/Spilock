import RPi.GPIO as GPIO
from time import sleep

def door_locked(buzzer, relay):
    GPIO.output(relay, GPIO.HIGH)
    GPIO.output(buzzer, GPIO.HIGH)
    sleep(0.5)
    GPIO.output(buzzer, GPIO.LOW)
    sleep(3)

def door_open(buzzer, relay):
    GPIO.output(relay, GPIO.LOW)
    GPIO.output(buzzer, GPIO.HIGH)
    sleep(0.5)
    GPIO.output(buzzer, GPIO.LOW)
    sleep(3)

def wrong_tap(buzzer, relay):
    GPIO.output(buzzer, GPIO.HIGH)
    sleep(0.3)
    GPIO.output(buzzer, GPIO.LOW)
    sleep(0.3)
    GPIO.output(buzzer, GPIO.HIGH)
    sleep(0.3)
    GPIO.output(buzzer, GPIO.LOW)
    sleep(0.3)
    GPIO.output(buzzer, GPIO.HIGH)
    sleep(0.3)
    GPIO.output(buzzer, GPIO.LOW)