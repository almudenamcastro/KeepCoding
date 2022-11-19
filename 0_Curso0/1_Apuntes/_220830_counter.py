def createCounter(ini=0):
    clicks = ini

    def counter():
        nonlocal clicks 
        clicks += 1
        return clicks

    return counter

# hacer el contador reutilizable, para poder consultar el valor sin aumentarlo y resetearlo. 

def createCounter2(ini=0):
    clicks = ini

    def counter(**kwargs):
        nonlocal clicks 

        if len(kwargs) ==0:
            clicks += 1
            return clicks

        if "tell" in kwargs: 
            return clicks

        if "reset" in kwargs:  
            clicks = kwargs["reset"]
            return clicks

    return counter


# Refactorizar para tener cada cosa en una función
# Este creador de una función con comportamiento y estado sería equivalente a una -> Clase

def createCounter3(ini=0):

    '''variables de estado -> Atributos'''
    clicks = ini
    
    ''' esto serían funciones de comportamiento -> Métodos'''
    
    def click():
        nonlocal clicks
        clicks +=1 
        return clicks

    def tell():
        return clicks
    
    def reset(v):
        nonlocal clicks
        clicks = v
        return clicks

    '''esto crea la infrastructura mínima (incluye el return) -> Constructor'''

    def counter(**kwargs):
        nonlocal clicks 

        if len(kwargs) ==0:
            return click()

        if "tell" in kwargs: 
            return tell()

        if "reset" in kwargs: 
            return reset(kwargs["reset"])

    return counter

'''
pruebas
'''
c=createCounter3()
print(c())
print(c())
print(c(tell=True))
print(c(reset=16))
print(c())


# Usamos una clase ahora

class Counter():
    '''esto sería el constructor (crea la infraestructura para que lo demás funcione). 
    self.clicks es la variable de estado'''

    def __init__(self, ini=0):
        self.clicks = ini

    '''y tendríamos también los métodos'''

    def click(self):
        self.clicks += 1
        return self.clicks
    
    def tell(self):
        return self.clicks

    def reset(self, v):
        self.clicks = v
        return self.clicks
    
'''
pruebas
'''
c=Counter()
print(c.click())
print(c.click())
print(c.tell())
print(c.reset(16))
print(c.click())
print(c.reset(0))
print(c.tell())