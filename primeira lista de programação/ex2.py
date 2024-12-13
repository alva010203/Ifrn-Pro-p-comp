valordesaque = float(input("Qual valor deseja sacar? "))

nota100 = valordesaque // 100
valordesaque = valordesaque - (nota100 * 100)

nota50 = valordesaque // 50
valordesaque = valordesaque - (nota50 * 50)

nota20 = valordesaque // 20
valordesaque = valordesaque - (nota20 * 20)

nota10 = valordesaque // 10
valordesaque = valordesaque - (nota10 * 10)

nota5= valordesaque // 5
valordesaque = valordesaque - (nota5 * 5)

nota2 = valordesaque // 2
valordesaque = valordesaque - (nota2 * 2)

moeda1 = valordesaque // 1
valordesaque = valordesaque - (moeda1 * 1)

moeda50 = valordesaque // 0.50
valordesaque = valordesaque - (moeda50 * 0.50)

moeda25 = valordesaque // 0.25
valordesaque = valordesaque - (moeda25 * 0.25)

moeda10 = valordesaque // 0.10
valordesaque = valordesaque - (moeda10 * 0.10)

moeda05 = valordesaque // 0.05
valordesaque = valordesaque - (moeda05 * 0.05)

moeda01 = round(valordesaque * 100)

if nota100 > 0:
 print(f"o valor de notas de 100 sera:{nota100:.0f}")
if nota50 > 0:
 print(f"o valor de notas de 50 sera:{nota50:.0f}")
if nota20 > 0:
 print(f"o valor de notas de 20 sera:{nota20:.0f}")
if nota10 > 0:
 print(f"o valor de notas de 10 sera:{nota10:.0f}")
if nota5 > 0:
 print(f"o valor de notas de 5 sera:{nota5:.0f}")
if nota2 > 0:
 print(f"o valor de notas de 2 sera:{nota2:.0f}")
if moeda1 > 0:
 print(f"o valor em moedas de 1 real sera:{moeda1:.0f}")
if moeda50 > 0:
 print(f"o valor em moedas de 50 centavos sera:{moeda50:.0f}")
if moeda25 > 0:
 print(f"o valor em moedas de 25 centavos sera:{moeda25:.0f}")
if moeda10 > 0:
 print(f"o valor em moedas de 10 centavos sera:{moeda10:.0f}")
if moeda05 > 0:
  print(f"o valor em moedas de moedas em 5 centavos sera:{moeda05:.0f}")
if moeda01 > 0:
 print(f"o valor em moedas de 1 centavo sera:{moeda01:.0f}") 











