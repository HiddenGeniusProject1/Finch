from BirdBrain import Finch
from time import sleep

bird = Finch()

def exercise1():
    bird.setBeak(80,20,60)
    sleep(1)
    bird.setBeak(0,0,0)

def exercise2():
    bird.setBeak(90,100,0)
    sleep(1)
    bird.setBeak(0,0,0)

def exercise3():
    bird.setTail(1,0,0,100)
    bird.setTail(4,0,0,100)
    sleep(2)
    bird.stopAll()

def exercise4():
    bird.setBeak(100,0,0)
    bird.setTail(1,0,100,0)
    bird.setTail(2,0,0,100)
    bird.setTail(3,100,100,0)
    bird.setTail(4,100,0,100)
    sleep(5)
    bird.setBeak(0,0,0)
    bird.stopAll()

def exercise5():
    userResponse = input("Which tail light (1-4) should be red? ")
    number = int(userResponse)
    bird.setTail(number,100,0,0)
    sleep(1)
    bird.stopAll()

def exercise6():
    userResponseOne = input("What amount of color (0-100) should red have?: ")
    userResponseTwo = input("What amount of color (0-100) should green have?: ")   
    userResponseThree = input("What amount of color (0-100) should blue have?: ")
    red = int(userResponseOne)
    green = int(userResponseTwo)
    blue = int(userResponseThree)
    bird.setBeak(red,green,blue)
    bird.setTail("all",red,green,blue)
    sleep(3)
    bird.setBeak(0,0,0)
    bird.stopAll()

def exercise7():
    userResponse = input("What should the side lengths be?: ")
    length = int(userResponse)
    bird.setTail("all",100,0,0)
    bird.setMove('F',length,50)
    bird.setTurn('R',90,80)
    bird.setTail("all",0,100,0)
    bird.setMove('F',length,50)
    bird.setTurn('R',90,80)
    bird.setTail("all",0,0,100)
    bird.setMove('F',length,50)
    bird.setTurn('R',90,80)
    bird.setTail("all",100,0,100)
    bird.setMove('F',length,50)
    bird.setTurn('R',90,80)
    bird.stopAll()
    

#exercise1()
#exercise2()
#exercise3()
#exercise4()
#exercise5()
#exercise6()
exercise7()
