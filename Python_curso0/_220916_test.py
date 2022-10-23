round(10*1.04, 2)


def onlyVowels(word):
    vowels="aeiou"
    resp=""
    for letter in word:
        if letter in vowels:
            resp += letter
    return resp

def applyToEach(function, *words):
    myList=[]
    for word in words:
        myList.append(function(word))
    return tuple(myList)

def second(*lis):
    maximun =max(lis)
    preMax=min(lis)
    for score in lis:
        if (score <maximun and score>preMax):
            preMax = score
    return preMax

def second2(*lis):
    arr = list(set(lis))
    arr.sort()
    return arr[-2]


def second3(*lis):
    first=max(lis)
    lis = list(lis)
    lis.remove(first)
    while first == max(lis):
        lis.remove(first)
    return max(lis)


def adder(n):
    return lambda x: x + n

test = adder(2)

class SWCharacter:
    def __init__(self, name):
        self.name = name

class Jedi (SWCharacter):
    def __init__(self, name, midic):
        super().__init__(name)
        self.midic = midic 

chewie =SWCharacter("Chewbacca")

def interes_anual(cantidad, interes):
    return cantidad*(1+interes/100)

def retorno(cantidad, interes, years):
    r=[]
    for year in range(years):
        cantidad=interes_anual(cantidad, interes)
        r.append(round(cantidad,2))

    return r