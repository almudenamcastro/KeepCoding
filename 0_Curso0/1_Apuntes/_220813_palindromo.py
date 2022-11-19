#import unidecodedata

def is_palindrome(string):
    temp=string.replace(" ", "").lower()
    return temp[::-1]==temp

def vocales(string):
    resultado=""
    for letter in string.lower():
        if letter in "aeiou":
            resultado += letter
    return resultado

#def vocales3(string):
#    resultado=""
#    i = 0
#    while i < len(string):
#        if string.lower()[i] in "aeiou":
#            resultado += string[i]
#        i += 1
#    return resultado

def vocales2(string):
    from unidecode import unidecode
    return [el for el in unidecode(string).lower() if el in "aeiou"]


def anagrama1(string1, string2):
    i=0
    while i <len(string1):
        if string1[i] in string2:
            string2=string2.replace(string1[i], "")
        i+=1
    return not bool(string2)   

def anagrama2(string1, string2):
    temp = list(string2)
    for letra in string1:
        if letra in temp:
            temp.remove(letra)
        else:
            return False
    return not bool(temp)

def anagrama3(string1, string2):
    temp = list(string2)
    for letra in string1:
        try:
            temp.remove(letra)
        except:
            return False
    return not bool(temp)

anagrama3("inglaterra", "integrarla")
anagrama3("mar", "rama")
anagrama3("oriol", "orlo")

def anagrama4(string1, string2):
    return sorted(string1)==sorted(string2)

def listarletras1(string):
    lista ={}
    for letra in string:
        if letra in lista:
            lista[letra] += 1
        else:
            lista[letra] = 1
    return lista

def listarletras2(string):
    lista=dict.fromkeys(set(string), 0)
    for letra in string:
            lista[letra] += 1
    return lista
        