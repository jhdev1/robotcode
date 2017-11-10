from sense_hat import SenseHat
sense = SenseHat()
sense.set_rotation(270)
from time import sleep

temp = str(sense.get_temperature())

speed=1.0

alphabet = []
for letter in range(65, 91):
    alphabet.append(chr(letter))
 

for letter in alphabet:
    print(letter)
    sense.show_letter(letter, text_colour=[255, 255, 255], back_colour=[0, 0, 0])
    sleep(speed)
	
sense.show_letter(' ', text_colour=[255, 255, 255], back_colour=[0, 0, 0])




