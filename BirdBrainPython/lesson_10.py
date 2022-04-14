from BirdBrain import Finch
bird = Finch()
from time import sleep

def exercise1():
    # This function makes the finch draw a square
    def drawSquare():
        for i in range(4):
            bird.setMove('F',15,50)
            bird.setTurn('R',90,50)
    for i in range(7):
        drawSquare()
        bird.setTurn('L',60,50)
    bird.stop()

exercise1()
