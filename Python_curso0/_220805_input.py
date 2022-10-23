# presentación
name = input("¿Cómo te llamas? ")
print("Hola", name)

#toma de datos
age = int(input ("¿cuántos años tienes? "))
year = int(input ("¿en qué año estamos? "))
birthday = input("¿ha sido ya tu cumpleaños (S/N)? ")

#calcular el año
if birthday == "S":
    birth_year= year - age
else:  
    birth_year= year-age-1

#presentar el resultado

print(name, ", naciste en", birth_year)

