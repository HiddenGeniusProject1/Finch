from BirdBrain import Finch
bird = Finch()

#Moves forward 25cm at a speed of 100, then moves backwards 25cm at a speed of 30.
def exercise1():
    bird.setMove('F',25,100)
    bird.setMove('B',25,30) 

#Repeats exercise1(). However, it then goes 25cm forward, then 40cm back, going back 15cm farther.
def exercise2():
    bird.setMove('F',25,100)
    bird.setMove('B',25,30)
    bird.setMove('F',25,100)
    bird.setMove('B',40,30)

#Makes the finch turn left in a circle, then right in a circle.
def exercise3():
    bird.setTurn('L',360,40)
    bird.setTurn('R',360,80)

#Creates a square using the code
def exercise4():
    bird.setMove('F',25,50)
    bird.setTurn('R',90,80)
    bird.setMove('F',25,50)
    bird.setTurn('R',90,80)
    bird.setMove('F',25,50)
    bird.setTurn('R',90,80)
    bird.setMove('F',25,50)
    bird.setTurn('R',90,80)

#Draws a pentagon
def exercise5():
    bird.setTurn('R',45,80)
    bird.setMove('F',30,50)
    bird.setTurn('R',90,80)
    bird.setMove('F',30,50)
    bird.setTurn('R',160,80)
    bird.setMove('F',45,50)
    bird.setTurn('R',160,80)
    bird.setMove('F',45,50)
    bird.setTurn('R',165,80)
    bird.setMove('F',45,50)

#exercise1()
#exercise2()
#exercise3()
exercise4()
#exercise5()
