###############################
# TABLA AND
###############################

print ("TABLA AND")
A = True
B = True
resultado = A and B
print ("| A   B | A AND B")
print ("-----------------------------")
print ("", int(A), " | ", int(B), " |    ", int(resultado))
A = True
B = False
resultado = A and B
print ("", int(A), " | ", int(B), " |    ", int(resultado))
A = False
B = True
resultado = A and B
print ("", int(A), " | ", int(B), " |    ", int(resultado))
A = False
B = False
resultado = A and B
print ("", int(A), " | ", int(B), " |    ", int(resultado))

###############################
# TABLA OR
###############################

print ("TABLA OR")
A = True
B = True
resultado = A or B
print ("| A   B | A AND B")
print ("-----------------------------")
print ("", int(A), " | ", int(B), " |    ", int(resultado))
A = True
B = False
resultado = A or B
print ("", int(A), " | ", int(B), " |    ", int(resultado))
A = False
B = True
resultado = A or B
print ("", int(A), " | ", int(B), " |    ", int(resultado))
A = False
B = False
resultado = A or B
print ("", int(A), " | ", int(B), " |    ", int(resultado))

###############################
# TABLA NOT
###############################

print ("TABLA NOT")
A = True
B = True
resultado = not(A)
print ("| A   B | A NOT B")
print ("-----------------------------")
print ("", int(A), " | ", int(B), " |    ", int(resultado))
A = True
B = False
resultado = not(A)
print ("", int(A), " | ", int(B), " |    ", int(resultado))
A = False
B = True
resultado = not(A)
print ("", int(A), " | ", int(B), " |    ", int(resultado))
A = False
B = False
resultado = not(A)
print ("", int(A), " | ", int(B), " |    ", int(resultado))