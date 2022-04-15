from BirdBrain import Finch
import time

bird = Finch()

#Sets the motors of the finch and turns fully around
def exercise1():
    bird.setMotors(100,-100)
    time.sleep(1)
    bird.stop()

#Asks the users for the value of the the left and right motors
def exercise2():
    userResponseLeft = input("On a scale of -100 to 100, what should the speed of the left wheel be?: ")
    userResponseRight = input("On a scale of -100 to 100, what should the speed of the right wheel be?: ")
    left = int(userResponseLeft)
    right = int(userResponseRight)
    bird.setMotors(left,right)
    time.sleep(2)
    bird.stop()

#Makes a figure-8
def exercise3():
    bird.setMotors(58,-58)
    time.sleep(1)
    bird.stop()
    bird.setMove('F',10,30)
    bird.setMotors(60,-60)
    time.sleep(1)
    bird.stop()

#Ask the user to enter the first initial of a color, making it green if they put g
def exercise4():
    color = input("Please enter a letter: ")
    if (color == 'g'):
        bird.setBeak(0,100,0)
    else:
        print('Sorry, that is not my favorite letter!')
    time.sleep(1)
    bird.stopAll()

#Asks the user to pick a direction for the finch
def exercise5():
    direction = input("Pick a direction (r or l): ")
    if (direction == 'r'):
        bird.setTurn('R',90,80)
    else:
        bird.setTurn('L',90,80)
        
#Asks the user to enter a slow speed
def exercise6():
    userResponse = input("Please enter a speed (-50 to 50): ")
    speed = int(userResponse)
    if (speed >= -50) and (speed<= 50):
        bird.setMotors(speed,speed)
        time.sleep(1)
        bird.stop()
    else:
        print("That speed is not a slow speed!")

#Aks the user for a speed, then sets it as its motors
def exercise7():
    userResponse = input("Please enter a speed between 0 to 50: ")
    speed = int(userResponse)
    if (speed >= 0) and (speed <= 50):
        bird.setMotors(speed,speed*2)
        time.sleep(1)
        bird.stop()
    else:
        print("Error")

#Asks the user for a type of dance
def exercise8():
    dance = input("Please enter one of these dances (moon walk, salsa, or  whip and nae nae: ")
    if (dance == 'moon walk'):
        bird.setTail(1,100,0,0)
        bird.setTail(2,0,100,0)
        bird.setTail(3,0,0,100)
        bird.setTail(3,100,0,100)
        bird.setMove('B',50,35)
        bird.stopAll()

    elif (dance == 'salsa'):
        bird.setTail(1,100,0,0)
        bird.setTail(2,0,100,0)
        bird.setTail(3,100,0,0)
        bird.setTail(4,0,100,0)
        bird.setMove('F',60,35)
        bird.setMove('B',60,35)
        bird.setTurn('R',360,70)
        bird.setMove('F',60,35)
        bird.setMove('B',60,35)
        bird.setTurn('L',360,70)
        bird.stopAll()

    elif (dance == 'whip and nae nae'):
        bird.setTail(1,100,0,0)
        bird.setTail(2,0,0,100)
        bird.setTail(3,100,0,0)
        bird.setTail(4,0,0,100)
        bird.setTurn('R',60,40)
        bird.setTurn('L',60,70)
        bird.setMove('B',50,50)
        bird.setTurn('R',60,40)
        bird.setTurn('L',60,70)
        bird.setTurn('L',60,40)
        bird.setTurn('R',60,70)
        bird.setMove('B',50,50)
        bird.stopAll()

    else:
        print("That dance is not an option!")

#exercise1()
#exercise2()
#exercise3()
#exercise4()
#exercise5()
#exercise6()
#exercise7()
exercise8()


