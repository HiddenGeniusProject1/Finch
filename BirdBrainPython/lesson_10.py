from BirdBrain import Finch
bird = Finch()
from time import sleep
import random

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

#Has the finch navigate through a maze
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
    #Have the finch automatially move itself rather than the user manually moving it
    #Make the finch turn 90 degrees whenever it spots an obstacle in its path
    #Use a while loop to repeatedly have the finch move until it sees an object
    #Create an additional function to serve in the code for the finch
    #Have the parent function continuously going straight, sub-function is turning
    
    #Algorithm: To navigate through a maze
        #While the front is clear
            #Move forward until the front is blocked
            #If the front is blocked
                #Turn to the left until the front is clear and not facing in the direction where it started

def turn(counter):
    while bird.getDistance() < 20:
        bird.setTurn('R',90,50)
    return counter + 1

#Fixed lesson on Exercise 4
def exercise4fixed(counter):

    while bird.getDistance() > 100:
        bird.setMove('F',5,50)
        if bird.getDistance() < 15:
            counter = turn(counter)
            
        #counter = counter + 1
            print(counter)

        """
        counter = counter + 1
        if counter == 3:
            turn()
            turn()
        counter = counter + 1
        if counter == 4:
            bird.setTurn('R',90,50)
        counter = 0
        if counter == 0:
            turn()
          """  
            
def exercise5():
    def drawSquare2(size):
        for i in range(4):
            bird.setMove('F',size,50)
            bird.setTurn('R',90,50)
    for i in range(5):
        drawSquare2(random.randint(5,20))

#Blinks the function until Button A is pressed
def exercise6():
    def blinkAll(red,green,blue):
        bird.setBeak(red,green,blue)
        bird.setTail("all",red,green,blue)
        sleep(1)
        bird.stopAll()
    while not bird.getButton('A'):
        blinkAll(100,50,20)
    bird.stopAll()

#Prints the orientation and blinks the lights until the Finch is not level
def exercise7():
    def blinkAll(red,green,blue):
        bird.setBeak(red,green,blue)
        bird.setTail("all",red,green,blue)
        sleep(1)
        bird.stopAll()

    def isLevel():
        return bird.getOrientation()

    while bird.getOrientation() == "Level":
        print(isLevel())
        blinkAll(100,50,20)
    bird.stopAll()
        

#exercise1()
#exercise2()
#exercise3()
#exercise4()
#exercise5()
#counter = 0
#exercise4fixed(counter)
#exercise6()
exercise7()
