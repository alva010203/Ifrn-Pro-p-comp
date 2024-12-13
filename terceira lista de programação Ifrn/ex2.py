
Elementos = int(input('Digite a quantidade máxima de elemtentos que a lista deve conter: '))

lista = []

#ADICIONA VALORES
while True:
    n = int(input('Digite os valores a serem inseridos:'))
    if n == 0: break
    lista.append(n)
    lista.sort()
    if len(lista) > Elementos:
        lista.pop()

    print(lista)
    
     
     
     
    
   
   
    