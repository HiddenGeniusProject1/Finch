from BirdBrain import Finch

bird = Finch()
def exercise1():
    print("Distance: ", bird.getDistance())

def exercise2():
    print("Number of Rotations Of Right Wheel: ", bird.getEncoder('R'))

def exercise3():
    print(type(bird.getEncoder('R')))

def exercise4():
    currentDistance = bird.getDistance()
    print(currentDistance)
    print(2*currentDistance)
    print(4*currentDistance)

def exercise5():
    lightSensorLeft = bird.getLight('L')
    lightSensorRight = bird.getLight('R')
    difference = lightSensorLeft-lightSensorRight
    print('Difference:',difference)

def exercise6():
    lightSensorLeft = bird.getLight('L')
    lightSensorRight = bird.getLight('R')
    mean = (lightSensorLeft+lightSensorRight)/2
    print('Mean:',mean)


exercise6()
    
