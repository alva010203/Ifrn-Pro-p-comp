import sys
num = int(input("Digite um número inteiro positivo: "))

if num <= 0: # verifica se o número é positivo.
    sys.exit('O número digitado não é inteiro positivo. ')

Armazen_num = num  # Armazena o número original para comparação

# Inicializa variáveis
soma = 0
n = 0

arm = num       # Conta o tanto de digitos
while arm > 0:
    arm //= 10
    n += 1

# Calcula a soma dos dígitos e eleva eles a potência
arm2 = num
while arm2 > 0:
    digito = arm2 % 10
    soma += digito ** n
    arm2 //= 10

# Verifica se a soma é igual ao número original
if soma == Armazen_num:
    print(f"{num} é um número de Armstrong.")
else:
    print(f"{num} não é um número de Armstrong.")
