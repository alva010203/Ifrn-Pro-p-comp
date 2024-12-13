import sys
num = int(input('informe um numero que seja inteiro positivo:'))

if num <= 0: # verifica se o número é positivo.
    sys.exit('O número digitado não é inteiro positivo. ')

else:
    n = 1
    triangular = False
    while True:
        tria_ngular = n * (n + 1) // 2    #n * (n + 1) sobre 2. 
        
        if tria_ngular == num:
            triangular = True
            break

        if tria_ngular > num:
            break
        n += 1

    if triangular:
        print(f'O número é triangular')

    else:
        print(f'O número não é triangular')