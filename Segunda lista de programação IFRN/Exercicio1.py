massa_i = float(input('Digite um numero: '))
tempo = 0 
massa_a = massa_i

while massa_a >= 0.5:  #transformação da massa.
    massa_a /= 2
    tempo += 50

horas = tempo // 3600
minutos = (tempo % 3600) // 60    # Tempo decorrido. 
segundos = tempo % 60

print(f'A massa inicial é igual a: {massa_i}')
print(f'Essa foi a massa obitida após a divisão: {massa_a}')
print(f'Tempo decorrido: {horas}:{minutos}:{segundos}')