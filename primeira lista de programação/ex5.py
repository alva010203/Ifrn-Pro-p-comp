min = int(input("Quantos minutos você passou no estacionamento? "))
hora = min // 60

if min <= 60:
 valor = 8.00
 print( valor )  

elif min >= 61 and min <= 120: 
   valor = 16.00
   print(valor)
 
elif min >= 121 and min <= 180:
  valor = 16.00 + 5.00
  print(valor)

elif min >= 181 and min <= 240:
  valor = 16.00 + 10.00
  print(valor)

elif hora >= 5 and hora <= 11:
 
 if min % 60 != 0 : 
   valor = (16.00 + 10.00) + (3.00 * (1 + hora - 4))                                                           
   print(valor)

 if min % 60 == 0: 
    valor = (16.00 + 10.00) + (3.00 * (hora - 4))
    print(valor)

elif min == 720:          #exatas 12 horas 
 valor = 26.00 + 24.00
 print(valor)

else: 
 print('O valor a ser pago será 30.00')   #valor fixo a ser pago depois das 12 horas.   # os valores finais estão de acordo com o que foi descrito na lista!!!




