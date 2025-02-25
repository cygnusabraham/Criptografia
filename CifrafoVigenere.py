def cifrar_vigenere(texto, clave):
    resultado = ""
    clave_repetida = (clave * (len(texto) // len(clave) + 1))[:len(texto)]

    for i, caracter in enumerate(texto):
        if caracter.isalpha():
            inicio = ord('A') if caracter.isupper() else ord('a')
            desplazamiento = ord(clave_repetida[i].lower()) - ord('a')
            nuevo_caracter = chr((ord(caracter) - inicio + desplazamiento) % 26 + inicio)
        else:
            nuevo_caracter = caracter
        resultado += nuevo_caracter
    return resultado


def descifrar_vigenere(texto_cifrado, clave):
    resultado = ""
    clave_repetida = (clave * (len(texto_cifrado) // len(clave) + 1))[:len(texto_cifrado)]

    for i, caracter in enumerate(texto_cifrado):
        if caracter.isalpha():
            inicio = ord('A') if caracter.isupper() else ord('a')
            desplazamiento = ord(clave_repetida[i].lower()) - ord('a')
            nuevo_caracter = chr((ord(caracter) - inicio - desplazamiento) % 26 + inicio)
        else:
            nuevo_caracter = caracter
        resultado += nuevo_caracter
    return resultado


# Texto a decifrar
texto_original = input("Introduce el texto a cifrar: ")
clave = input("Introduce la clave: ")

texto_cifrado = cifrar_vigenere(texto_original, clave)
print("Texto cifrado:", texto_cifrado)

texto_descifrado = descifrar_vigenere(texto_cifrado, clave)
print("Texto descifrado:", texto_descifrado)
