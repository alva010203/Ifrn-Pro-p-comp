import math, random

n = int(input('Digite o número de elementos:'))

lista = [random.randint(0,99) for _ in range(n)]

#media 
media = sum(lista) / n

#mediana
ordem = sorted(lista)
if n % 2 == 0:
    mediana = (ordem[n // 2 - 1] + ordem[n // 2]) / 2
else:
    mediana = ordem [n // 2]

#para impar valor sera o central e para um numero de elementos pares vai ser os dois centrais

#variancia
variancia = sum((x - media) ** 2 for x in lista) / n

#desvio padraoo
desvp = math.sqrt(variancia)

print(f'lista:{lista}')
print('---')
print(f'Media:{media}')
print('---')
print(f'mediana:{mediana}')
print('---')
print(f'variancia:{variancia}')
print('---')
print(f'desvio padrão:{desvp}')