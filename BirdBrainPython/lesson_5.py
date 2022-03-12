from BirdBrain import Finch
import time

bird = Finch()

def exercise1():
    userResponse = input("Pick either button A or B to flash: ")
    if bird.getButton(userResponse):
        bird.setBeak(0,100,0)
    else:
        bird.setBeak(100,0,0)
    time.sleep(1)
    bird.stopAll()

def exercise2():
    if bird.getButton('B'):
        bird.setMove('B',50,60)
    else:
        bird.setMove('F',50,60)

def extraChallenge():
    if bird.getButton('Logo'):
        bird.setTurn('L',360,60)
    else:
        bird.setTurn('R',90,60)

def exercise3():
    print(bird.getDistance())
    if bird.getDistance() < 30:
        bird.setTail("all",0,0,100)
    else:
        bird.setTail("all",100,0,0)
    time.sleep(2)
    bird.stopAll()

def exercise4():
    print(bird.getDistance())
    if bird.getDistance() > 20:
        bird.setMove('F',40,50)
    else:
        bird.setMove('B',50,50)

def exercise5():
    while bird.getDistance() < 30:
        bird.setBeak(100,0,0)
    bird.setBeak(0,100,0)
    time.sleep(1)
    bird.stopAll()

def exercise6():
    print(bird.getDistance())
    while bird.getDistance() > 35:
        bird.setMove('F',40,40)
    bird.stop()

def exercise7():
    while bird.getDistance() > 20:
        bird.setTail("all",0,0,100)
        time.sleep(3)
        bird.setTail("all",100,0,100)
        time.sleep(3)
    bird.stopAll()

def exercise8():
    while bird.getDistance() < 27:
        bird.setBeak(100,0,0)
        bird.setTail("all",100,0,0)
    bird.setBeak(0,0,100)
    bird.setTail(1,0,100,0)
    bird.setTail(2,100,0,100)

#exercise1()
#exercise2()
#extraChallenge()
#exercise3()
#exercise4()
#exercise5()
#exercise6()
#exercise7()
exercise8()
