import random , math

n = 0
while n < 7 or n > 60:
    print("Digite elementos (entre 7 e 60): ", end="")
    n = int(input())

# Faz numeros aleatorios e não repetidos
lista_numeros = random.sample(range(1, 61), n)

# Calcular o fatorial de um número
fatorial = lambda x: 1 if x == 0 else x * fatorial(x - 1)

total_combinacoes = fatorial(60) // (fatorial(n) * fatorial(60 - n))

# combinações possíveis de 6 números
combinacoes = []
lista_para_combinacoes = lista_numeros

# pilha com a combinação vazia
pilha = [([], lista_para_combinacoes)]

# Processa a pilha
while pilha:
    combinacao_atual, sublista = pilha.pop()
    if len(combinacao_atual) == 6:
        combinacoes.append(combinacao_atual)
    else:
        for i in range(len(sublista)):
            nova_combinacao = combinacao_atual + [sublista[i]]
            pilha.append((nova_combinacao, sublista[i + 1:]))

#combinação
combinacoes = [sorted(comb) for comb in combinacoes]

# Salva na lista
with open('numeros_escolhidos.txt', 'w') as f:
    f.write(';'.join(map(str, lista_numeros)))

# Salva as combinações
with open('combinacoes.txt', 'w') as f:
    for combinacao in combinacoes:
        f.write(';'.join(map(str, combinacao)) + '\n')

# Sena, Quina e Quadra
prob_sena = 0
prob_quina = 0
prob_quadra = 0

if n >= 6:
    prob_sena = (fatorial(n) // (fatorial(6) * fatorial(n - 6))) / total_combinacoes

if n >= 5:
    prob_quina = (fatorial(n) // (fatorial(5) * fatorial(n - 5))) / total_combinacoes

if n >= 4:
    prob_quadra = (fatorial(n) // (fatorial(4) * fatorial(n - 4))) / total_combinacoes


print(f"Total de combinações geradas: {len(combinacoes)}")
print(f"Probabilidade de acertar a sena: {prob_sena:.10f}")
print(f"Probabilidade de acertar a quina: {prob_quina:.10f}")
print(f"Probabilidade de acertar a quadra: {prob_quadra:.10f}")