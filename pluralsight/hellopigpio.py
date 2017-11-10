import RPi.GPIO as GPIO
import time

pin = 7
GPIO.setmode(GPIO.BOARD)
GPIO.setup(pin, GPIO.OUT)

print("Starting blinker")

sleep = 0.5

for n in range(0,60):
    print(n)
    GPIO.output(pin,GPIO.HIGH)
    time.sleep(sleep)
    GPIO.output(pin,GPIO.LOW)
    time.sleep(sleep)
	
GPIO.cleanup()

print("All Done")
