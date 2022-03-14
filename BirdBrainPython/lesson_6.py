from BirdBrain import Finch
import time

bird = Finch()

def exercise1():
    userResponse = input("What is your name?: ")
    bird.print("Hi" + userResponse)
    time.sleep(5)

def exercise2():
    bird.setPoint(1,1,1)
    bird.setPoint(2,2,1)
    bird.setPoint(3,3,1)
    bird.setPoint(4,4,1)
    bird.setPoint(1,5,1)
    bird.setPoint(5,1,1)
    bird.setPoint(4,2,1)
    bird.setPoint(2,4,1)
    bird.setPoint(5,5,1)
    time.sleep(1)
    bird.stopAll()

def exercise3():
    for i in range(6):
        bird.setMove('F',60,65)
        bird.setMove('B',60,65)

def exercise4():
    for i in range(5):
        bird.setPoint(i+1,i+1,1)
        time.sleep(.5)
    bird.stopAll()

def exercise5():
    for i in range(5):
        bird.setPoint(1,i+1,1)
        time.sleep(.5)
    for i in range(5):
        bird.setPoint(i+1,5,1)
        time.sleep(.5)
    for i in range(5):
        bird.setPoint(5,i+1,1)
        time.sleep(.5)
    for i in range(5):
        bird.setPoint(i+1,1,1)
        time.sleep(.5)
    bird.stopAll()

def exercise6():
    bird.setDisplay([0,1,0,1,0,
                     0,0,0,0,0,
                     0,0,0,0,0,
                     1,0,0,0,1,
                     0,1,1,1,0])
    time.sleep(1)
    bird.stopAll()

def exercise7():
    for i in range(5):
        bird.setDisplay([0,1,0,1,0,
                         0,0,0,0,0,
                         0,0,0,0,0,
                         1,0,0,0,1,
                         0,1,1,1,0])
        time.sleep(1)
        bird.setDisplay([0,1,0,1,0,
                         0,0,0,0,0,
                         0,0,0,0,0,
                         0,1,1,1,0,
                         1,0,0,0,1])
        time.sleep(1)
    bird.stopAll()

def exercise8():
    userResponse = input("Ask for a number of sides and the shape will be drawn: ")
    shape = int(userResponse)
    number = str(shape)
    if shape == 3:
        for i in range(3):
            bird.print(number)
            bird.setMove('F',30,60)
            bird.setTurn('L',120,50)
        bird.stop()
    elif shape == 4:
        for i in range(4):
            bird.print(number)
            bird.setMove('F',45,60)
            bird.setTurn('L',90,60)
        bird.stop()
    elif shape == 5:
        for i in range(5):
            bird.print(number)
            bird.setMove('F',50,60)
            bird.setTurn('L',72,60)

    elif shape == 2:
        print("ERROR -> Those sides don't make a shape!")
            
        
       
#exercise1()
#exercise2()
#exercise3()
#exercise4()
#exercise5()
#exercise6()
#exercise7()
exercise8()
