def iterPower(base, exp):
    '''
    base: int or float.
    exp: int >= 0
 
    returns: int or float, base^exp
    '''
    # Your code here
    i=0
    total = 1
    while i<exp:
        total *= base
        i += 1
    return total
    
def recurPower(base, exp):
    '''
    base: int or float.
    exp: int >= 0
 
    returns: int or float, base^exp
    '''
    # Your code here
    if exp == 0:
        return 1
    if exp == 1:
        return base
    return base*recurPower(base, exp-1)

def recurPowerNew(base, exp):
    '''
    base: int or float.
    exp: int >= 0

    returns: int or float; base^exp
    '''
    # Your code here
    if exp == 0:
        return 1
    if exp == 1:
        return base
    if exp % 2 == 0:
        return recurPowerNew(base*base, exp/2.0)
    if exp % 2 != 0:
        return base*recurPowerNew(base, exp-1)

def gcdIter(a, b):
    '''
    a, b: positive integers
    
    returns: a positive integer, the greatest common divisor of a & b.
    '''
    # Your code here
    div = min(a,b)
    while div > 0:
        if a % div == 0 and b % div == 0:
            return div
        elif div == 1:
            return div
        else:
            div -= 1
            
def gcdRecur(a, b):
    '''
    a, b: positive integers
    
    returns: a positive integer, the greatest common divisor of a & b.
    '''
    # Your code here
    
    #Invert b and a if b is larger
    if b > a:
        temp = a
        a = b
        b = temp
    print("a and b are: "+str(a)+" and "+str(b))  
    #return a is b == 0, by definition of Euclids algorithm
    if b == 0:
        return a
    #q is amount of times that b fits in a
    q = a/b
    #div is the divisor
    div = a/q
    print("q is "+str(q)+", div is "+str(div)+" & remainder is: "+str(a%b))
    if a%b == 0:
        return div
    return gcdRecur(b, a%b)

def lenIter(aStr):
    '''
    aStr: a string
    
    returns: int, the length of aStr
    '''
    # Your code here
    i = 0
    for c in aStr:
        i += 1
    return i


def lenRecur(aStr):
    '''
    aStr: a string
    
    returns: int, the length of aStr
    '''
    # Your code here
    if aStr[:] == '':
        return 0
    if aStr[1:] == '':
        return 1
    else:
        return 1+lenRecur(aStr[1:])

#L5 Problem 8    
def isIn(char, aStr):
    '''
    char: a single character
    aStr: an alphabetized string
    
    returns: True if char is in aStr; False otherwise
    '''
    # Your code here
    if aStr[:] == '':
        return False
    if aStr[1:] == '':
        if char == aStr:
            return True
        else:
            return False
    else:
        if char == aStr[len(aStr)/2]:
            return True
        elif char < aStr[len(aStr)/2]:
            return isIn(char,aStr[0:len(aStr)/2])
        else:   
            return isIn(char,aStr[len(aStr)/2:])


def semordnilap(str1, str2):
    '''
    str1: a string
    str2: a string
    
    returns: True if str1 and str2 are semordnilap;
             False otherwise.
    '''
    # Your code here
    if len(str1) != len(str2):
        return False
    if str1 == str2 and (len(str1) <= 1 and len(str2) <= 1):
        return True
    if str1 == str2:
        return False
    if str1[:1] == str2[-1:]:
        return semordnilap(str1[1:-1],str2[1:-1:])
    
           

    
