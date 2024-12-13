valor_i = int(input('informe o valor inicial da P.A: '))
razão = int(input('informe a razao da P.A: '))
quantidade_de_elements = int(input('Digite a quantidade de elementos presentes na P.A '))

P_A = []
#Gera os elemntos da P.A
for i in range(quantidade_de_elements):
    elemento = valor_i + i * razão
    P_A.append(elemento)
print(f'os elementos da P.A são: {P_A}')


#identifica se é constante, crescente ou decrescente. 

if razão == 0:
    tipo_pa = "constante"

elif razão > 0:
    tipo_pa = "crescente"

else:
    tipo_pa = "decrescente"


print(f'A P.A é do tipo :{tipo_pa}')


soma = sum(P_A)
print(f'Essa é a soma da P.A: {soma}')

posicao = int(input('Digite a posição que voce quer saber o valor:'))

if 1 <= posicao <= quantidade_de_elements:
    valor_ele = P_A[posicao - 1]
    print(f'O valor do elemento na posição ({posicao}) é:{valor_ele}')

else:
    print('posição invalida')