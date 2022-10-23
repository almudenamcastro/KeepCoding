month_length = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

# pedir fecha
day = int(input("dia: "))
month = int(input("mes: "))
year = int(input("año: "))

# ¿año bisiesto?

def bisiesto (year):
  if year%4 != 0:
    return False
  if year%400 == 0: 
    return True
  elif year%100 ==0: 
    return False
  else: 
    return True
  
if bisiesto(year): 
  month_length[1]=29

#contador meses anteriores
i = 0
day_count = 0

while i < month - 1:
#   day_count = day_count + month_length[i]
    day_count += month_length[i]
    i += 1

#calcular dia
day_count += day

#imprimir resultado
print(day_count)

