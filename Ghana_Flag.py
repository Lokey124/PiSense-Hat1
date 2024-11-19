from sense_hat import SenseHat
import time

s = SenseHat()




s.low_light = True
s.set_rotation(270)


green = 	(0,0,128)
red = (128,0,128)
yellow = (139,69,19)
black = (0,0,0)

def ghana_flag_logo():
    
    G = green
    R = red
    Y = yellow
    B = black
    
    logo = [
    R, R, R, R, R, R, R, R,
    R, R, R, R, R, R, R, R,
    R, R, R, R, R, R, R, R,
    Y, Y, Y, B, B, Y, Y, Y,
    Y, Y, Y, B, B, Y, Y, Y,
    G, G, G, G, G, G, G, G,
    G, G, G, G, G, G, G, G,
    G, G, G, G, G, G, G, G,
    ]
    return logo




images = [ghana_flag_logo, ]
count = 0

while True:
    s.set_pixels(images[count % len(images)]())
    time.sleep(1)
    count += 1  

