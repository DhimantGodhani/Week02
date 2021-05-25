import math
from datetime import datetime


def calcArea(radius):
    circleArea = math.pi * pow(radius, 2)
    return circleArea


def NameInReverse(firstName, lastName):
    return "The name in reverse order is " + str(lastName) + " " + str(firstName)


def getDateTime():
    currentDateTime = datetime.now()
    return currentDateTime
