gabarito = ['A', 'C', 'B', 'A', 'E', 'D', 'D', 'C', 'A', 'A']
lista_alunos = [ ['Aluno 01', 'B', 'D', 'E', 'E', 'C', 'D', 'A', 'B', 'C', 'D'],
 ['Aluno 02', 'C', 'D', 'A', 'B', 'D', 'A', 'A', 'C', 'B', 'E'],
 ['Aluno 03', 'A', 'A', 'B', 'D', 'C', 'E', 'E', 'A', 'A', 'C'],
 ['Aluno 04', 'B', 'B', 'C', 'C', 'D', 'E', 'D', 'D', 'E', 'E'],
 ['Aluno 05', 'B', 'B', 'D', 'A', 'A', 'E', 'B', 'D', 'E', 'C'],
 ['Aluno 06', 'C', 'C', 'D', 'E', 'B', 'B', 'C', 'D', 'E', 'A'],
 ['Aluno 07', 'B', 'A', 'A', 'B', 'B', 'C', 'D', 'E', 'A', 'B'],
 ['Aluno 08', 'D', 'E', 'A', 'B', 'B', 'C', 'C', 'D', 'A', 'A'],
 ['Aluno 09', 'A', 'A', 'A', 'C', 'B', 'D', 'D', 'E', 'D', 'C'],
 ['Aluno 10', 'B', 'B', 'D', 'E', 'C', 'D', 'C', 'E', 'B','A'] ]

resultado = []

for aluno in lista_alunos:
    nome = aluno[0]
    resposta = aluno[1:]
    acertos = 0 
    for i in range(len(gabarito)):
        if resposta[i] == gabarito[i]:
            acertos += 1
    resultado.append((nome,acertos,resposta))

#ordena a lista em ordem decrescente
resultado.sort(key=lambda x: x[1], reverse=True)
   
for nome, acertos,resposta in resultado:
    print(f'Nome: {nome}')
    print(f'Gabarito:  {" ".join(map(str, gabarito))}')
    print(f'Respostas: {" ".join(map(str, resposta))}')
    print(f'Número de Acertos: {acertos}')
    print('---')  