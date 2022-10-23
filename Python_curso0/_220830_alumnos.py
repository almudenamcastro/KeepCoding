class Subject():
    def __init__(self, name, level="A1"):
        self.name = name
        self.level = level
        self.price = ""

    def __str__(self):
        return "Asignatura {}, nivel {}, {} €/mes".format(self.name, self.level,self.price*4) 
    
    def __repr__(self):
        return self.__str__()

class Persona():

    ''' atribbutos de clase: aquí podría haber atributos que se crean incluso sin pasar por init'''

    def __init__(self, nombre, apellido):
        ''' atributos de instancia '''
        self.nombre = nombre
        self.apellido = apellido 
        self.email = "" 
        self.asignaturas = []

    def __str__(self):
        return "{}: {} {} - {}". format(type(self).__name__, self.nombre, self.apellido, self.email)

    def __repr__(self):
        return self.__str__()

    def alta_asignatura(self, asignatura):
        if not isinstance(asignatura, Subject):
            raise Exception ("{} debe ser de clase Asignatura".format(asignatura))
        if asignatura in self.asignaturas: #compruebo que no está matriculado
            raise Exception ("ya existe la asignatura{}".format(asignatura))
        return self.asignaturas.append(asignatura)

    def baja_asignatura(self, asignatura):
        if not asignatura in self.asignaturas: #compruebo que está matriculado
            raise Exception ("No se encuentra la asignatura {}".format(asignatura))
        return self.asignaturas.remove(asignatura)

class Teacher(Persona):

    def __init__(self, nombre, apellido, nif, sueldobase=200):
        super().__init__(nombre, apellido) #    Persona.__init__(self, nombre, apellido)
        self.nif = nif
        self.sueldobase = sueldobase

    @property
    def sueldo(self):
        return self.sueldobase + len(self.asignaturas)*200

class Student(Persona):
    pass

'''
pruebas
'''

ingles=Subject("inglés")
aleman=Subject("alemán", "C2")
ingles.price=7.50
aleman.price=10.00

roberto = Student("Roberto", "Pérez")
roberto.email="email@r.com"
roberto.alta_asignatura(ingles)
roberto.alta_asignatura(aleman)

jm = Teacher("Juan", "Martín")
jm.sueldo()
jm.alta_asignatura(ingles)
jm.sueldo()
