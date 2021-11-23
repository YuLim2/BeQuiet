import RPi.GPIO as GPIO
import time
GPIO.stemode(GPIO.BCM)
PIN_NUM = 26
CHECK = 0
GPIO.setup(PIN_NUM,GPIO.IN)
try:
    while True:
        if GPIO.input(PIN_NUM) == CHECK:
            #데이터 보내
            
