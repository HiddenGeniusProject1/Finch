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

#Creates multiple circles in a pattern for the finch
def exercise2():
    def drawCircle():
        bird.setMotors(0,50)
        sleep(3)
    for i in range(4):
        drawCircle()
        bird.setMove('F',15,50)
    bird.stop()
            
#Tracks the line sensors of what color it detects until the distance is less than 20
def exercise3():
    def lineTrack():
        white = (bird.getLine('L') + bird.getLine('R'))/2
        black = (bird.getLine('L') + bird.getLine('R'))/2
        threshold =  (white+black)/2
        if (bird.getLine('L') < threshold) or (bird.getLine('R') < threshold):
            print("black")
        else:
            print("white")
    while (bird.getDistance() > 20):
        lineTrack()
        bird.setMove('F',30,40)
    bird.stop()

def exercise4():
    def wallFollowing():
        while bird.getDistance() > 20:
            bird.setMove('F',20,50)
        bird.setTurn('R',90,50)
        while bird.getDistance() > 10:
            bird.setMove('F',10,50)
        bird.setTurn('L',90,50)
        while bird.getDistance() > 16:
            bird.setMove('F',12,50)
        bird.setTurn('L',90,50)
        while bird.getDistance() > 10:
            bird.setMove('F',5,50)
        bird.setTurn('R',90,50)
        bird.setMove('F',45,50)
        bird.print("YOUDIDIT")
    wallFollowing()


#exercise1()
#exercise2()
#exercise3()
exercise4()
