import random,sys


linhas = int(input("Digite a quantidade de linhas na matriz: "))
colunas = int(input("Digite a quantidade de elementos em cada colunas: "))

if linhas <= 0 or colunas <= 0:
    sys.exit('Tente um número que seja POSITIVO ou que seja diferente de ZERO')

else:
# matriz aleatoria
    matriz = [[random.randint(1, 9999) for _ in range(colunas)] for _ in range(linhas)]

# matriz original
    print("Matriz original:")
    for linha in matriz:
        print(linha)

    print('-----------')
# matriz transposta
    matriz_transposta = [[matriz[x][y] for x in range(linhas)] for y in range(colunas)]

# matriz transposta
    print("Matriz transposta:")
    for linha in matriz_transposta:
        print(linha)

