import RPI.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
PIN_NUM = 26
BUZ = 17
CHECK_ON = 0
GPIO.setup(PIN_NUM, GPIO.IN)
GPIO.setup(BUZ, GPIO.OUT)
try:
    while True:
        if GPIO.input(PIN_NUM) == CHECK_ON:
            GPIO.output(BUZ, GPIO.HIGH)
            time.sleep(0.1)
        else:
            GPIO.output(BUZ, GPIO.LOW)
        finally :
            GPIO.cleanup()
