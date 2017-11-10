from sense_hat import SenseHat
sense = SenseHat()
sense.set_rotation(270)

red = (255,0,0)
brown = (102,51,0)
orange = (204, 102, 0)

temp = str(sense.get_temperature())

speed=0.06

letter = "Hi from Kai Hammond.  The temperature is: " + temp + " degrees Celsius"
sense.show_letter('s', text_colour=[255, 255, 255], back_colour=[0, 0, 0])
