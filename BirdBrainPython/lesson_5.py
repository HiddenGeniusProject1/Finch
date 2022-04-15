from BirdBrain import Finch
import time

bird = Finch()

#Asks the user to pick between button A or B to flash
def exercise1():
    userResponse = input("Pick either button A or B to flash: ")
    if bird.getButton(userResponse):
        bird.setBeak(0,100,0)
    else:
        bird.setBeak(100,0,0)
    time.sleep(1)
    bird.stopAll()

#Moves the finch if button B is pressed
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

#Prints distance of finch, then lights up tail depending on distance
def exercise3():
    print(bird.getDistance())
    if bird.getDistance() < 30:
        bird.setTail("all",0,0,100)
    else:
        bird.setTail("all",100,0,0)
    time.sleep(2)
    bird.stopAll()

#Moves the finch forwards or backward depending on distance
def exercise4():
    print(bird.getDistance())
    if bird.getDistance() > 20:
        bird.setMove('F',40,50)
    else:
        bird.setMove('B',50,50)

#Sets color while distance is less than 30 
def exercise5():
    while bird.getDistance() < 30:
        bird.setBeak(100,0,0)
    bird.setBeak(0,100,0)
    time.sleep(1)
    bird.stopAll()

#Prints distance, then has it move while it is more than a distance of 35 
def exercise6():
    print(bird.getDistance())
    while bird.getDistance() > 35:
        bird.setMove('F',40,40)
    bird.stop()

#Flashes the the light back and forth while distance is greater than 20
def exercise7():
    while bird.getDistance() > 20:
        bird.setTail("all",0,0,100)
        time.sleep(3)
        bird.setTail("all",100,0,100)
        time.sleep(3)
    bird.stopAll()

#Makes the finch light up and turns the finch around while distance is less than 80
def exercise8():
    while bird.getDistance() < 80:
        bird.setBeak(100,0,0)
        bird.setTail("all",100,0,0)
    bird.setBeak(0,0,100)
    bird.setTail(1,0,100,0)
    bird.setTail(2,100,0,100)
    bird.setTail(3,100,0,0)
    bird.setTail(4,80,80,50)
    bird.setTurn('R',2160,90)
    bird.stopAll()

#Runs the code while button A isn't pressed
def exercise9():
    while not bird.getButton('A'):
        bird.setTail(1,0,100,0)
        time.sleep(0.1)
        bird.setTail(3,0,100,0)
        time.sleep(0.1)
        bird.stopAll()
        time.sleep(0.1)

#While Button B isn't pressed, the finch moves back and forth
def exercise10():
    while not bird.getButton('B'):
        bird.setMove('F',50,50)
        bird.setMove('B',50,50)
    bird.stop()

#Sets the beak to red first, but due to the while loop, it passes the code and goes down to the rest of the code
def exercise11():
    bird.setBeak(100,0,0)
    while bird.getDistance() < 30:
        pass
    bird.setBeak(0,100,0)
    time.sleep(1)
    bird.stopAll()

#While button A is not pressed, an if and elif statement will be ran depending on the distances.
def exercise12():
    while not bird.getButton('A'):
        if (bird.getDistance() > 65):
            bird.setMove('F',50,60)
        elif (bird.getDistance() <=65):
            bird.setMove('B',50,60)
            bird.setTurn('R',90,60)
    bird.stop()



#exercise1()
#exercise2()
#extraChallenge()
#exercise3()
#exercise4()
#exercise5()
#exercise6()
#exercise7()
#exercise8()
#exercise9()
#exercise10()
#exercise11()
exercise12()


