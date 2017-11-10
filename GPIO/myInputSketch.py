import RPi.GPIO as GPIO
from sys import exit

#set up GPIO using BCM numbering
GPIO.setmode(GPIO.BCM)

#setup GPIO using Board numbering
#GPIO.setmode(GPIO.BOARD)


GPIO.setup(23, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)
GPIO.setup(24, GPIO.IN, pull_up_down = GPIO.PUD_UP)

def printFunction(channel):
    print("Button 1 pressed!")
    print("Note how the bouncetime affects the button press")

GPIO.add_event_detect(23, GPIO.RISING, callback=printFunction, bouncetime=300)

print("READY...")

while True:
    try:
        GPIO.wait_for_edge(24, GPIO.FALLING)
        print("Button 2 Pressed")
        GPIO.wait_for_edge(24, GPIO.RISING)
        print("Button 2 Released")
        GPIO.cleanup()
    except KeyboardInterrupt:
        exit()


## Remove Event
# GPIO.remove_event_detect(23)

## https://makezine.com/projects/tutorial-raspberry-pi-gpio-pins-and-python/
