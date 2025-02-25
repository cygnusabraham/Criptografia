def cifrar_cesar(texto, desplazamiento):
    resultado = ""
    for caracter in texto:
        if caracter.isalpha():
            inicio = ord('A') if caracter.isupper() else ord('a')
            nuevo_caracter = chr((ord(caracter) - inicio + desplazamiento) % 26 + inicio)
        else:
            nuevo_caracter = caracter
        resultado += nuevo_caracter
    return resultado

def descifrar_cesar(texto_cifrado, desplazamiento):
    return cifrar_cesar(texto_cifrado, -desplazamiento)

# Entrada del usuario
texto_original = input("Introduce el texto a cifrar: ")
desplazamiento = int(input("Introduce el desplazamiento: "))

texto_cifrado = cifrar_cesar(texto_original, desplazamiento)
print("Texto cifrado:", texto_cifrado)
