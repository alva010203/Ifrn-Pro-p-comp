FORCA = "MACACO"

tent = 6
tenta_errada = ""
palavra_oculta = "_" * len(FORCA)

print("Bem-vindo ao Jogo da Forca")
print("Você tem 6 tentativas.")
print("Palavra", palavra_oculta)

while tent > 0 and "_" in palavra_oculta:
    letra = input("Digite uma letra: ").upper()

    if letra in tenta_errada or letra in palavra_oculta:
        print("Você já tentou essa letra.")
        continue
    
    if letra in FORCA:
        nova_palavra_oculta = ""
        for i in range(len(FORCA)):
            if FORCA[i] == letra:
                nova_palavra_oculta += letra
            else:
                nova_palavra_oculta += palavra_oculta[i]
        palavra_oculta = nova_palavra_oculta
        print("Acertou! Palavra", palavra_oculta)
    
    else:
        tenta_errada += letra
        tent -= 1
        print(f"Errou! você ainda tem {tent} vidas.")
        print("Letras erradas:", tenta_errada)

if "_" not in palavra_oculta:
    print("Parabéns!!! Você foi perfeito.")
else:
    print(F"Que pena! A palavra era:{FORCA} ")