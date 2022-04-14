from BirdBrain import Finch

bird = Finch()

#Prints distance of finch
def exercise1():
    print("Distance: ", bird.getDistance())

#Prints the number of rotations for right wheel
def exercise2():
    print("Number of Rotations Of Right Wheel: ", bird.getEncoder('R'))

#Prints the type of method bird.getEncoder is
def exercise3():
    print(type(bird.getEncoder('R')))

#Prints out the distances of the finch in different numerical values
def exercise4():
    currentDistance = bird.getDistance()
    print(currentDistance)
    print(2*currentDistance)
    print(4*currentDistance)

#Prints the different of the left and right light sensors
def exercise5():
    lightSensorLeft = bird.getLight('L')
    lightSensorRight = bird.getLight('R')
    difference = lightSensorLeft-lightSensorRight
    print('Difference:',difference)

#Prints the mean of the left and right light sensors
def exercise6():
    lightSensorLeft = bird.getLight('L')
    lightSensorRight = bird.getLight('R')
    mean = (lightSensorLeft+lightSensorRight)/2
    print('Mean:',mean)


exercise6()
    
