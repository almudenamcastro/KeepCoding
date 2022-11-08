# IF, ELIF
# We can use if and elif to set a condition. 
# The code will only be read if the condition is met. 

# La diferencia entre if y elif es que: 
# if siempre se evalúa (independientemente de la condición anterior)
# elif solo se evalúa si la condición anterior era False

def elifif(x):
    if x > 1: #si es mayor que 1
        print("es mayor que 1, if")
    elif x > 0: #si NO es mayor que 1 Y ES mayor que 0 
        print("es menor que 1 y mayor que 0, elif")
    if x> 0: #si es mayor que 0 (luego también es mayor que 1)
        print("es mayor que 0, if") 
    else: 
        print("else")

# CALCULAR EL IRPF EN FUNCIÓN DE ESTADO CIVIL Y SUELDO

# Queremos crear un programa que calcule la retención IRPF según estado civil, hijos y sueldo

# Pedir datos: 
estado_civil = input ("Situación (1, 2, 3): ")
hijos = int(input("número de hijos: "))
sueldo = float (input("Sueldo: "))
  
# Calcular exención:
if estado_civil == '1':
    if hijos <1: 
        exencion = 0
    elif hijos == 1: 
        exencion = 15947
    else: 
        exencion = 17100 
elif estado_civil == '2':
    if hijos <1: 
        exencion = 15546
    elif hijos == 1: 
        exencion = 16481
    else: 
        exencion=17634 
elif estado_civil == '3': 
    if hijos <1: 
        exencion = 14000
    elif hijos == 1: 
        exencion = 14516
    else: 
        exencion = 15093

# calcular base a retener:
base = sueldo - exencion

# calcular retención:
ret = 0

#tramos irpf
tramos = [0, 12450, 20200, 35200, 60000]
percent = [0.19, 0.24, 0.3, 0.37, 0.45]

#vamos tramo a tramo reteniendo el porcentaje correspondiente. 
if base - tramos[4] > 0: 
    ret = (base - tramos[4]) * percent[4]
    base = tramos[4]

if base - tramos[3] > 0:
    ret = ret + (base - tramos[3]) * percent[3]
    base = tramos[3]

if base - tramos[2] > 0:
    ret=ret + (base - tramos[2]) * percent[2]
    base = tramos[2]

if base - tramos[1] > 0:
    ret=ret + (base - tramos[1]) * percent[1] 
    base = tramos[1]

if base - tramos[0] >0:
    ret = ret + (base - tramos[0]) * percent[0]
    base = tramos[0]

#mostrar resultados
print ("Retención: \t", ret)