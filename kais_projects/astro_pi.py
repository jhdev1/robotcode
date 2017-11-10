from sense_hat import SenseHat
sense = SenseHat()
sense.set_rotation(270)

midnightblue = (25,25,112)
yellow = (255,255,0)

temp = str(sense.get_temperature())

speed=0.03

message = "Hi from Kai Hammond.  The temperature is: " + temp + " Celsius"
sense.show_message (message, speed, text_colour=yellow, back_colour=midnightblue)

