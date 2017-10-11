import math
import random
from matplotlib.pyplot import *

class Dot:
    def __init__(self, x = 0.0, y = 0.0):
        self.x = x
        self.y = y

def distanceOf2Dot(dot1, dot2):
    return ((dot2.x - dot1.x)**2 + (dot2.y - dot1.y)**2) ** 0.5

def get13dot(dot1, dot2):
    return Dot(dot2.x / 3 + 2*dot1.x / 3, dot2.y / 3 + 2*dot1.y / 3)

def get23dot(dot1, dot2):
    return Dot(2*dot2.x / 3 + dot1.x / 3, 2*dot2.y / 3 + dot1.y / 3)

def getSlopeOfLineSegment(dot1, dot2):
    return (dot2.y - dot1.y) / (dot2.x - dot1.x)

def get33dot(dot1, dot2):
    C = Dot()
    cos60 = math.cos(math.radians(60))
    sin60 = math.sin(math.radians(60))
    C.x = dot1.x +  (dot2.x - dot1.x) * cos60 - (dot2.y - dot1.y) * sin60
    C.y = dot1.y +  (dot2.x - dot1.x) * sin60 + (dot2.y - dot1.y) * cos60
    return C

def one1(dot1, dot2):
    dotArray = []
    m = get13dot(dot1, dot2)
    n = get23dot(dot1, dot2)
    c = get33dot(m, n)
    dotArray.append(dot1)
    dotArray.append(m)
    dotArray.append(c)
    dotArray.append(n)
    dotArray.append(dot2)
    return dotArray

def drawDot(dA):
    for i in range(len(dA) - 1):
        plot([dA[i].x, dA[i+1].x], [dA[i].y, dA[i+1].y])
    show()

def printArray(dA):
    for i in range(len(dA)):
        print i, dA[i].x, dA[i].y

if __name__ == "__main__":
    f = random.randrange(0.0, 10.0)
    print f
    a = Dot(float(f), float(f+1))
    b = Dot(6.0, 5.0)
    A = one1(a, b)
    printArray(A)
    drawDot(A)
