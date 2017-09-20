import math
from matplotlib.pyplot import *

class Dot:
    def __init__(self, x = 0.0, y = 0.0):
        self.x = x
        self.y = y

def getTwoDotDistance(dot1, dot2):
    """
    get the distance that between two dots.
    it returns of  sqrt ((x2-x1)**2 + (y2 - y1)**2)
    """
    return ((dot2.x - dot1.x)**2 + (dot2.y - dot1.y)**2) ** 0.5

def getMiddleOfLineSegment(dot1, dot2):
    """
    get the middle values of line segment.
    it returns (x, y)
    """
    return (dot2.x + dot1.x) * 0.5, (dot2.y + dot1.y) * 0.5

def getSlope(dot1, dot2):
    """
    get the slope of line (dot1,dot2)
    """
    return (dot2.y - dot1.y) / (dot2.x - dot1.x)

def getIntercept(dot1, k):
    """
    get the intercept of line (dot1,dot2)
    """
    return dot1.y - k * dot1.x

def getSlopeAndIntercept(dot1, dot2):
    """
    get the slope and intercept of line that (dot1,dot2)
    """
    k = getSlope(dot1, dot2)
    return k, getIntercept(dot1, k)

def getXY1(dot1, dot2):
    """
    get the one-third of line segment (dot1,dot2)
    """
    k = getSlope(dot1, dot2)
    b = getIntercept(dot1, k)
    c = k / b
    _a = Dot(0, b)
    _b = Dot(c, 0)
    _c = getTwoDotDistance(_a, _b)
    _d = getTwoDotDistance(dot1, dot2) / 3

    return (_d * c) / _c + dot1.x, (_d * b ) / _c + dot1.y

def getXY2(dot1, dot2):
    """
    get the two-third of line segment (dot1,dot2)
    """
    k = getSlope(dot1, dot2)
    b = getIntercept(dot1, k)
    c =  k / b 
    _a = Dot(0, b)
    _b = Dot(c, 0)
    _c = getTwoDotDistance(_a, _b)
    _d = getTwoDotDistance(dot1, dot2) / 3

    return 2*(_d * c) / _c + dot1.x, 2*(_d * b ) / _c + dot1.y
    
def getXY3(dot1, dot2):
    A = dot1
    B = dot2
    C = Dot()

    R = getTwoDotDistance(A,B)
    C.x = dot1.x + R * math.cos(math.radians(90))
    C.y = dot1.y + R * math.sin(math.radians(90))
    return C.x, C.y

def one(dot1, dot2):

    a = dot1
    b = dot2
    twofloatnumber = getXY1(a, b)
    m = Dot(twofloatnumber[0], twofloatnumber[1])
    twofloatnumber = getXY2(a, b)
    n = Dot(twofloatnumber[0], twofloatnumber[1])
    tmp = getXY3(m, n)
    c = Dot(tmp[0], tmp[1])
    '''paint the view
    '''
    plot([a.x, m.x], [a.y, m.y])
    plot([m.x, c.x], [m.y, c.y])
    plot([n.x, c.x], [n.y, c.y])
    plot([n.x, b.x], [n.y, b.y])
    show()

if __name__ == "__main__":
    a = Dot(2.0, 3.0)
    b = Dot(3.0, 4.0)
    tmp = getXY1(a, b)
    c = Dot(tmp[0], tmp[1])
    one(a, b)
