import sys
num_1 = int(input('Informe o Primeiro digito inteiro positivo:'))
num_2 = int(input('Informe o Segundo digito inteiro positivo:'))

if (num_1 or num_2) <= 0:
    sys.exit('informe um número positivo inteiro.')

while num_2 != 0:
    num_1 , num_2 = num_2, num_1 % num_2
        

print(f'o MDC dos números inseridos é {num_1}')


