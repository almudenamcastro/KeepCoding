         
"""            
def retencion1(sueldo):
    #tramos irpf
    tramos = [12450, 20200, 35200, 60000]
    percent = [0.19, 0.24, 0.30, 0.37, 0.45]

    for i in range(len(tramos)):
        if sueldo <= tramos[i]:
            return percent[i]
      
    return percent[i+1]
    
    
def exencion1(estado, hijos):
    
    exencion=[[0, 15947, 17100],[15546, 16481, 17634],[14000, 14516, 15093]]
    
    if hijos > 2:
        hijos = 2

    return exencion[estado-1][hijos]


"""

def exencion(estado, hijos):
    
    exencion={"1":[0, 15947, 17100],"2":[15546, 16481, 17634],"3":[14000, 14516, 15093]}
    
    if hijos > 2:
        hijos = 2

    return exencion[estado][hijos]


def retencion(sueldo):
    #tramos irpf
    tramos = [[0,0],[12450,0.19], [20200,0.24], [35200,0.30], [60000,0.37], [300000, 0.45], [float("inf"), 0.47]]

    for rango, porcentaje in tramos:
        if sueldo <= rango:
            return porcentaje
    

"""

# pedir datos. 

estado_civil = int(input ("Situación (1, 2, 3): "))
hijos = int(input("número de hijos: "))
sueldo = float (input("Sueldo: "))


# calcular base a retener.
base = sueldo - exencion(estado_civil, hijos)
ret = retencion(base)



#mostrar resultados
print ("Retención: \t", ret)
"""