import math, sys

termo_inicial = int(input('Digite o termo inicial da P.G:'))
razao = float(input('Digite a razão:'))

quantidade_elements =  int(input('Digite a quantidade de elementos: '))
if quantidade_elements <= 0:
    sys.exit('Digite um valor inteiro positivo.')

# calcula elementos P.G
elementos = []
for i in range(quantidade_elements):
    elemento = termo_inicial * (razao ** i)
    elementos.append(elemento)

for i, valor in enumerate(elementos):#enumerate vai colocar indice em cada elemento.
    print(f'Elemento {i+1}: {valor}')

#determina o tipo da P.G
if razao ==  1:
    tipo_d_pg = 'Constante'
elif razao > 1:
    tipo_d_pg = "Crescente"
elif razao < -1 or (razao < 0 and quantidade_elements % 2 == 0):
    tipo_d_pg = "Oscilante"
else:
    tipo_d_pg = "Decrescente"   

print(f'A P.G é do tipo: {tipo_d_pg}')

#soma elementos
soma_dos_elementos = sum(elementos)
print(f'A soma dos elementos é {soma_dos_elementos}')

n = int(input("Digite a posição (n) do elemento da P.G. que deseja consultar: "))

if n <= 0 or n > quantidade_elements:
    print("Posição inválida.")
else:
    valor_n = termo_inicial * (razao ** (n - 1))
    print(f"O valor do elemento na posição {n} é: {valor_n}")