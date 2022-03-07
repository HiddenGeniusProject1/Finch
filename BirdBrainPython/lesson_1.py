from BirdBrain import Finch
bird = Finch()
def exercise1():
    bird.setMove('F',25,100)
    bird.setMove('B',25,30)

def exercise2():
    bird.setMove('F',25,100)
    bird.setMove('B',25,30)
    bird.setMove('F',25,100)
    bird.setMove('B',40,30)

def exercise3():
    bird.setTurn('L',360,40)
    bird.setTurn('R',360,80)

def exercise4():
    bird.setMove('F',25,50)
    bird.setTurn('R',90,80)
    bird.setMove('F',25,50)
    bird.setTurn('R',90,80)
    bird.setMove('F',25,50)
    bird.setTurn('R',90,80)
    bird.setMove('F',25,50)
    bird.setTurn('R',90,80)

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
