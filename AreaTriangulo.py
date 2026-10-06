# Area triangulo
    # Pregunta por base
base=float(input("Dime la base: "))
# Pregunta por altura
altura=float(input("Dime la altura: "))
# Hace la operación y lo guarda en la variable "area"
area=(base*altura/2)
# Si es incompatible da error
if base<=0 or altura<=0:
    print ("error")
# Muestra la variable
else:
    print (area)
# FIN