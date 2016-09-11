import math

def polysum(n,s):
    perimeter = n*s
    area=(0.25*n*s*s)/(math.tan(math.pi/n))
    suma = perimeter * perimeter + area
    return round(suma,4)