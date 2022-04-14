from BirdBrain import Finch
from time import sleep
import math

bird = Finch()

def exercise1():
    while not bird.getOrientation() == "Upside down":
        bird.setMotors(100,50)
    bird.stop()

def exercise2():
    while not bird.getButton('A'):
        if bird.getOrientation() == "Tilt left":
            bird.setBeak(0,100,0)
        elif bird.getOrientation() == "Tilt right":
            bird.setBeak(100,0,100)
        elif bird.getOrientation() == "Beak down":
            bird.setBeak(0,0,100)
        elif bird.getOrientation() == "Beak up":
            bird.setBeak(100,0,0)
        elif bird.getOrientation() == "Level":
            bird.setBeak(100,100,0)
        elif bird.getOrientation() == "Upside down":
            bird.setBeak(0,100,100)
        elif bird.getOrientation() == "In between":
            bird.setBeak(50,80,20)
    bird.stopAll()

def exercise3():
    while not bird.getLight('L') <= 20:
        print(bird.getAcceleration())
        sleep(3)
    bird.stopAll()

def exercise4():
    while not bird.getButton('A'):
        accelX, accelY, accelZ = bird.getAcceleration()
        bird.setMotors(50,0)
        x = accelX
        x = x*50
        y = accelY
        y = y*50
        z = accelZ
        z = z*50
        if x < 0:
            x = x*-1
        if y < 0:
            y = y*-1
        if z < 0:
            z = z*-1
        if x > 100:
            x = 100
        if y > 100:
            y = 100
        if z > 100:
            z = 100
        x = int(x)
        y = int(y)
        z = int(z)
        print(x,y,z)
        bird.setBeak(x,y,z)
    bird.stopAll()

def exercise5():
    userResponse = input("Input the amount of seconds: ")
    seconds = int(userResponse)
    accelX, accelY, accelZ = bird.getAcceleration()
    x = accelX
    y = accelY
    z = accelZ
    a = math.sqrt(x*x + y*y + z*z)
    while not a > 20:
        sleep(seconds)
        bird.setBeak(100,0,0)
        bird.setTail(1,100,0,0)
        bird.setTail(2,0,0,100)
        bird.setTail(3,100,0,0)
        bird.setTail(4,0,0,100)
        bird.setMove('F',40,50)
        bird.setMove('B',40,50)
        bird.setTurn('R',360,50)
    bird.stopAll()
        

#exercise1()
#exercise2()
#exercise3()
#exercise4()
exercise5()
        
