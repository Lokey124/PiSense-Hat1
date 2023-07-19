from sense_hat import SenseHat
import time

s = SenseHat()




s.low_light = True
s.set_rotation(270)
angles = [0, 90, 180, 270, 0, 90, 180, 270]

green = (255,215,0)
darkgreen= (0,100,0)
lightgreen = (0,255,127)
mintgreen = (0,255,0)
teal =(0,255,0)
red = (255,0,0) 
blue = (30,144,255)
darkblue = (70,130,180)
hotpink = (255,0,255)
violet = (128,0,128)
yellow = (255,255,0)
orange = (255,140,0)
brown = (139,69,19)
black = (0,0,0)
white = (255,255,255)
nothing = (0,0,0)

def leonardo_logo():
    
    Y = brown
    U = blue
    S = darkblue
    D = black
    V = green
    X = darkgreen
    W = yellow
    I = orange
    B = hotpink
    O = nothing
    logo = [
    O, O, O, V, V, V, V, O,
    O, S, U, U, D, U, D, O,
    O, O, V, V, V, V, V, V,
    O, Y, V, V, V, D, V, V,
    Y, Y, V, Y, Y, Y, O, O,
    Y, V, V, W, I, W, V, O,
    O, Y, V, I, I, I, O, O,
    O, O, V, O, O, V, O, O,
    ]
    return logo

def raphael_logo():
    
    Y = brown
    U = red
    C = violet
    X = darkgreen
    Q = lightgreen
    V = green
    W = yellow
    I = orange
    D = black
    O = nothing
    logo = [
    O, O, O, Q, Q, Q, Q, O,
    O, U, U, U, D, U, D, O,
    O, Q, Q, Q, Q, Q, Q, Q,
    O, Y, Q, Q, D, D, Q, Q,
    Y, Y, Q, Y, Y, Y, O, O,
    Y, Q, Q, W, I, W, Q, O,
    O, Y, Q, I, I, I, O, O,
    O, O, Q, O, O, Q, O, O,
    ]
    return logo

def michealangelo_logo():
    
    Y = brown
    G = teal
    L = mintgreen
    X = darkgreen
    V = green
    W = yellow
    I = orange
    P = teal
    D = black
    E = white
    O = nothing
    logo = [
    O, O, O, G, G, G, G, O,
    O, I, I, I, D, I, D, O,
    O, O, G, D, G, G, G, G,
    O, Y, G, D, D, D, G, G,
    Y, Y, G, Y, Y, Y, O, O,
    Y, G, G, W, I, W, G, O,
    O, Y, G, I, I, I, O, O,
    O, O, G, O, O, G, O, O,
    ]
    return logo

def donatello_logo():
    
    Y = brown
    X = darkgreen
    V = green
    V = green
    W = yellow
    I = orange
    P = teal
    D = black
    C = violet
    J = hotpink
    O = nothing
    logo = [
    O, O, O, X, X, X, X, O,
    O, J, J, J, D, J, D, O,
    O, O, X, X, X, X, X, X,
    O, Y, X, X, D, X, X, X,
    Y, Y, X, Y, Y, Y, O, O,
    Y, X, X, W, I, W, X, O,
    O, Y, X, I, I, I, O, O,
    O, O, X, O, O, X, O, O,
    ]
    return logo


images = [leonardo_logo, raphael_logo, michealangelo_logo, donatello_logo,]
count = 0

while True:
    s.set_pixels(images[count % len(images)]())
    time.sleep(2)
    count += 1
