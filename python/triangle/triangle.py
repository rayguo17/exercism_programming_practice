def equilateral(sides):
    #assume they have abc
    if(not istriangle(sides)):
        return False
    a= sides[0]
    b=sides[1]
    c=sides[2]
    if (a==0) or (b==0) or (c==0):
        return False
    if (a==b) and (b==c):
        return True
    return False


def isosceles(sides):
    if(not istriangle(sides)):
        return False
    a= sides[0]
    b=sides[1]
    c=sides[2]
    if (a==0) or (b==0) or (c==0):
        return False
    if (a==b) or (a==c) or (b==c):
        return True
    return False


def scalene(sides):
    if(not istriangle(sides)):
        return False
    a= sides[0]
    b=sides[1]
    c=sides[2]
    if (a==0) or (b==0) or (c==0):
        return False
    if (a==b) or (a==c) or (b==c):
        return False
    return True

def istriangle(sides):
    a= sides[0]
    b=sides[1]
    c=sides[2]
    if(a+b<c) :
        return False
    if(a+c<b):
        return False
    if(b+c<a):
        return False 
    return True