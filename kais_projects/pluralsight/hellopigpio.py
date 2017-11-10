import RPi.GPIO as GPIO
import time

pin = 7
GPIO.setmode(GPIO.BOARD)
GPIO.setup(pin, GPIO.OUT)
GPIO.setwarnings(False)


def blink (seconds):
    print(seconds)
    GPIO.output(pin,GPIO.HIGH)
    time.sleep(seconds)
    GPIO.output(pin,GPIO.LOW)
    time.sleep(seconds)    
    
for n in range(0,5):
    blink(n)
    


GPIO.cleanup()

