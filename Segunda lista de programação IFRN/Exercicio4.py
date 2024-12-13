for n in range (1 , 1000000):
    if n % 2 == 0 or 5 == 0: #ver se o numero é multiplo de 2 e 5
        sum = 0 
        num = n
                #soma, decompoe e verifica            
        while num > 0:   
            Dig = num % 10 
            sum += Dig ** 5
            num  //= 10
        if sum == n:
            print(n)
print('Os números acima corresponde aos números menores que 1 milhão, multiplos dos números 2 e 5 e que se encaixam na soma de potencias de 5.')