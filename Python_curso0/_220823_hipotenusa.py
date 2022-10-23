import math

def hypotenuse(c1, c2=0):
    if c2 == 0:
        c2 = c1
    return math.sqrt(c1*c1 + c2*c2)

cateto1 = 3
cateto2 = 4

hp = hypotenuse(cateto1, cateto2)