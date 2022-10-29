from re import I

ALPHABET = list("abcdefghijklmnñopqrstuvwxyz")

def cesar_v0(letter, n): 
    if n > len(ALPHABET):
       raise ValueError("introduce un número menor que {}".format(len(ALPHABET)))
    for i in range(len(ALPHABET)):
            if letter.lower() == ALPHABET[i]:
                try:
                    return ALPHABET[i+n]
                except:
                    return ALPHABET[i+n-len(ALPHABET)]

def cesar(letter, n): 
    i = (ALPHABET.index(letter.lower()) + n)%len(ALPHABET)
    return ALPHABET[i]

def cifrar(string, n):
    clear_string=""
    for letter in string:
        clear_string += cesar(letter, n)
    return clear_string

def metacifrar(n):
    '''sirve para inyectar un parámetro y crear una función euivalente a cifrar'''
    def cifrarn (string):
        clear_string=""
        for letter in string:
            clear_string += cesar(letter, n)
        return clear_string
    return cifrarn


    cosa = ["elemento1", "elemento2", "elemento3", "elemento4"]

    print ("iba yo por la calle y me encontré una {}, es lo mejor para poder {}. Estaba {} y todo me pareció muy {}".format(*cosa))

vector1=[1,2,3,4]
vector2=[2,3,4,0]

sum([vector1[i]*vector2[i] for i in range(len(vector1))])

def f(ht):
    b=0
    for elt in ht:
        b = b + elt
    return b