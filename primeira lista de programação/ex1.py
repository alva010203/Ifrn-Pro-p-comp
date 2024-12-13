import math, sys
A = float(input('informe um valor: '))
B = float(input('informe um valor: '))
C = float(input('informe um valor: '))

if A < B + C and B < A + C  and C < A + B:
 print('As medidas acima podem fomar um triângulo:')

 if A == B ==  C:
   print('Equilatero')
 elif A != B != C != A:
   print('Escaleno')
 else:
   print('Isórceles')
else:
 print('As medidas acima não podem formar um triângulo!')
 sys.exit()
 

ANGULO_1 = math.degrees(math.acos((B**2 + C **2 - A**2 )/(2*B*C)))
ANGULO_2 = math.degrees(math.acos((A**2 + C **2 - B**2 )/(2*A*C)))
ANGULO_3 = 180 - ANGULO_1 - ANGULO_2

print('Esses são os angulos do triângulo:')
print(round(ANGULO_1))
print(round(ANGULO_2))
print(round(ANGULO_3))

print('O seu angulo é classificado como:')
if ANGULO_1 > 90 or ANGULO_2 > 90 or ANGULO_3 > 90:
 print('Obtuso')
elif ANGULO_1 == 90 or ANGULO_2 == 90 or ANGULO_3 == 90:
 print('Retângulo')
else:
 print('Agudo') 