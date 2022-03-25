from BirdBrain import Finch
import time
import random

bird = Finch()

def exercise1():
    while not bird.getButton('A'):
        bird.setBeak(0,0,bird.getLight('R'))
        bird.setTail("all",0,bird.getLight('L'),0)
        
    bird.stopAll
"""    
def exercise2():
    while not bird.getButton('A'):
        bird.setBeak(0,0, 100-bird.getLight('R'),0)
        bird.setTail("all",0,bird.getLight('L')-100,0)
        
    bird.stopAll()
"""
def exercise2():
    while not bird.getButton('A'):
        bird.setBeak(0,100 - bird.getLight('R'),0)    # Control beak with right light sensor
        bird.setTail("all",0,0,100 - bird.getLight('L'))

    bird.stopAll()

def exercise3():
    while not bird.getButton('A'):
        bird.setMotors(bird.getLight('R'),bird.getLight('L'))

    bird.stopAll()

def exercise4():
    dark = 15
    while (bird.getLight('L') > dark):
        bird.setMove('F',40,50)
    bird.stopAll()

def exercise5():
    dark = 20
    while (bird.getLight('L') < dark):
        bird.setBeak(100,0,0)
        bird.setTail("all",100,0,0)
        bird.setTurn('R',720,70)
        bird.setMove('F',50,80)
        bird.setMove('B',50,80)
    bird.setBeak(0,100,0)
    bird.setTail("all",0,100,0)
    time.sleep(6)

def exercise6():
    for i in range(5):
        bird.setMotors(random.randint(-100,100), random.randint(-100,100))
        time.sleep(2)
    bird.stopAll()

def exercise7():
    dark = 25
    while (bird.getLight('L') < dark):
        bird.setTail(1,random.randint(0,100),random.randint(0,100),random.randint(0,100))
        bird.setTail(2,random.randint(0,100),random.randint(0,100),random.randint(0,100))
        bird.setTail(3,random.randint(0,100),random.randint(0,100),random.randint(0,100))
        bird.setTail(4,random.randint(0,100),random.randint(0,100),random.randint(0,100))
        time.sleep(1)
    bird.stopAll()

def exercise8():
    dark = 25
    while (bird.getLight('L') < dark):
        bird.setTail(1,random.randint(0,100),random.randint(0,100),random.randint(0,100))
        bird.setTail(2,random.randint(0,100),random.randint(0,100),random.randint(0,100))
        bird.setTail(3,random.randint(0,100),random.randint(0,100),random.randint(0,100))
        bird.setTail(4,random.randint(0,100),random.randint(0,100),random.randint(0,100))
        time.sleep(random.randint(0,5))
    bird.stopAll()

def exercise9():
    dark = 25
    while (bird.getLight('R') > dark):
           bird.setBeak(100,0,0)
           bird.setTurn('R',360,50)
           time.sleep(random.randint(0,2))
           bird.setBeak(0,100,0)
           time.sleep(1)
    bird.stopAll()
                      
           
           

#exercise1()
#exercise2()
#exercise3()
#exercise4()
#exercise5()
#exercise6()
#exercise7()
#exercise8()
exercise9()
          

