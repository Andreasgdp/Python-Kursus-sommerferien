import random
from random import randint
import math


def setup():
    frameRate(5)
    background(255)
    size(500,500)
    
def draw():
    background(255)
    rotate(random.random())
    r = rect(width/2, height/2, 20, 20)



def keyPressed():
    if key == 's':
        saveFrame("fuckingFirkanter-####.jpg")
