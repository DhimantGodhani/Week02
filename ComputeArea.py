from utils import calcArea


def inputData():
    radius = float(input('Enter the radius of circle in centimeters: '))
    return radius


def printData(circleArea, radius):
    print("The area of circle with radius " + str(radius) + " is " + format(circleArea, ".2f") + " sq. cm.")


def main():
    print('Compute Area Program')
    print('This program is designed to compute area of the circle.')
    radius = inputData()
    circleArea = calcArea(radius)
    printData(circleArea, radius)


main()
