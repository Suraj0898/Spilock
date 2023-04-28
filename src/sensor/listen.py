import speech_recognition as sr
from datetime import date
import RPi.GPIO as GPIO
from time import sleep

from utils.microphone import microphone


def listen():
    relay = 26

    r = sr.Recognizer()
    mic = sr.Microphone(device_index=1)

    print("start")

    while True:
        with mic as source:
            r.adjust_for_ambient_noise(source)
            r.dynamic_energy_threshold = 3000

            try:
                print("Please answer the question")
                r.pause_threshold = 1
                audio = r.listen(source, timeout=100.0)
                response = r.recognize_google(audio)
                my_microphone = microphone()
                my_microphone.set_response(response)
                print(my_microphone.get_response())
            except sr.UnknownValueError:
                print("Did not recognize the answer, Please repeat again!")
            audio = r.listen(source)
    return my_microphone
