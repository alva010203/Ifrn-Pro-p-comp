x_inicial = int(input("Digite a coordenada X inicial: "))
y_inicial = int(input("Digite a coordenada Y inicial: "))
movimentos = input("Digite a string de movimentos: ").upper()

# variáveis
x = x_inicial
y = y_inicial
movimentos_validos = ""
cont_movimentos = 0

# Processar movimentos
for movimento in movimentos:
    if movimento == 'U':
        y += 1
        movimentos_validos += movimento
        cont_movimentos += 1
    elif movimento == 'D':
        y -= 1
        movimentos_validos += movimento
        cont_movimentos += 1
    elif movimento == 'R':
        x += 1
        movimentos_validos += movimento
        cont_movimentos += 1
    elif movimento == 'L':
        x -= 1
        movimentos_validos += movimento
        cont_movimentos += 1
    elif movimento == 'O':
        x -= 1
        y += 1
        movimentos_validos += movimento
        cont_movimentos += 1
    elif movimento == 'N':
        x += 1
        y += 1
        movimentos_validos += movimento
        cont_movimentos += 1
    elif movimento == 'E':
        x += 1
        y -= 1
        movimentos_validos += movimento
        cont_movimentos += 1
    elif movimento == 'W':
        x -= 1
        y -= 1
        movimentos_validos += movimento
        cont_movimentos += 1

#quadrante inicial
if x_inicial > 0 and y_inicial > 0:
    quadrante_inicial = "O robô começou no quadrante 1"
elif x_inicial < 0 and y_inicial > 0:
    quadrante_inicial = "O robô começou no quadrante 2"
elif x_inicial < 0 and y_inicial < 0:
    quadrante_inicial = "O robô começou no quadrante 3"
elif x_inicial > 0 and y_inicial < 0:
    quadrante_inicial = " O robô começou no quadrante 4"
elif x_inicial == 0 and y_inicial == 0:
    quadrante_inicial = "Origem"
elif x_inicial == 0:
    quadrante_inicial = "O robô começou no Eixo Y"
elif y_inicial == 0:
    quadrante_inicial = "O robô começou no Eixo X"

# quadrante final
if x > 0 and y > 0:
    quadrante_final = "O robô terminou no quadrante 1"
elif x < 0 and y > 0:
    quadrante_final = "O robô terminou no quadrante 2"
elif x < 0 and y < 0:
    quadrante_final = "O robô terminou no quadrante 3"
elif x > 0 and y < 0:
    quadrante_final = "O robô terminou no quadrante 4"
elif x == 0 and y == 0:
    quadrante_final = "Origem"
elif x == 0:
    quadrante_final = "O robô terminou no Eixo Y"
elif y == 0:
    quadrante_final = "O robô terminou no Eixo X"


print(f"Posição inicial: ({x_inicial}, {y_inicial})")
print(f"Posição final: ({x}, {y})")
print(f"Quantidade de movimentos válidos: {cont_movimentos}")
print(f"Movimentos válidos: {movimentos_validos}")
print(f"Quadrante inicial: {quadrante_inicial}")
print(f"Quadrante final: {quadrante_final}")
