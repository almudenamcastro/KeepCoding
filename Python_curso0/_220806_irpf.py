# pedir datos. 

estado_civil = input ("Situación (1, 2, 3): ")
hijos = int(input("número de hijos: "))
sueldo = float (input("Sueldo: "))


  
# calcular exención.
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
else: 
    if hijos <1: 
        exencion = 14000
    elif hijos == 1: 
        exencion = 14516
    else: 
        exencion = 15093 


# calcular base a retener.
base = sueldo - exencion


# calcular retención.
ret = 0

#tramos irpf
tramos = [0, 12450, 20200, 35200, 60000]
porcent = [0.19, 0.24, 0.3, 0.37, 0.45]

tramo4 = 60000
p4 = 0.45
tramo3 = 35200
p3 = 0.37
tramo2 = 20200
p2 = 0.30
tramo1 = 12450
p1 = 0.24
tramo0 = 0
p0 = 0.19



if base - tramo4 > 0: 
    ret = (base - tramo4) * p4
    base = tramo4

if base - tramo3 > 0:
    ret = ret + (base - tramo3) * p3
    base = tramo3

if base - tramo2 > 0:
    ret=ret + (base - tramo2) * p2
    base = tramo2

if base - tramo1 > 0:
    ret=ret + (base - tramo1) * p1 
    base = tramo1

if base - tramo0 >0:
    ret = ret + (base - tramo0) * p0
    base = tramo0



#mostrar resultados
print ("Retención: \t", ret)
