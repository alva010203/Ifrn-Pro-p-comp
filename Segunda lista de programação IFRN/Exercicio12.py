texto = input('Digite uma frase para criptografar: ')
chave = input('Digite uma chave para a criptografia: ')

# tamanho do texto
chave = (chave * (len(texto) // len(chave) + 1))[:len(texto)]

# Converte o texto para maiúsculas
texto = texto.upper()
chave = chave.upper()

# Criptografia
texto_criptografado = []

for i in range(len(texto)):
    t = texto[i]
    c = chave[i]

    if 'A' <= t <= 'Z':
        deslocamento = ord(c) - ord('A')
        novo_char = chr(((ord(t) - ord('A') + deslocamento) % 26) + ord('A'))
        texto_criptografado.append(novo_char)
    else:
        texto_criptografado.append(t)

texto_criptografado = ''.join(texto_criptografado)
print('Texto criptografado:', texto_criptografado)

# Descriptografia
texto_descriptografado = []

for i in range(len(texto_criptografado)):
    t = texto_criptografado[i]
    c = chave[i]

    if 'A' <= t <= 'Z':
        deslocamento = ord(c) - ord('A')
        novo_char = chr(((ord(t) - ord('A') - deslocamento) % 26) + ord('A'))
        texto_descriptografado.append(novo_char)
    else:
        texto_descriptografado.append(t)

texto_descriptografado = ''.join(texto_descriptografado)
print('Texto descriptografado:', texto_descriptografado)