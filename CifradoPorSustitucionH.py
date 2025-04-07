import random

# Diccionario de sustitución homofónica: múltiples números para cada letra
homofonic_dict = {
    'A': [11, 12],
    'B': [13],
    'C': [14, 15],
    'D': [16],
    'E': [17, 18, 19],
    'F': [20],
    'G': [21],
    'H': [22],
    'I': [23, 24],
    'J': [25],
    'K': [26],
    'L': [27],
    'M': [28],
    'N': [29],
    'O': [30, 31],
    'P': [32],
    'Q': [33],
    'R': [34],
    'S': [35, 36],
    'T': [37, 38],
    'U': [39],
    'V': [40],
    'W': [41],
    'X': [42],
    'Y': [43],
    'Z': [44],
}

# Invertir el diccionario para descifrado
decrypt_dict = {}
for letter, codes in homofonic_dict.items():
    for code in codes:
        decrypt_dict[code] = letter

def cifrar(mensaje):
    mensaje = mensaje.upper().replace(" ", "")
    cifrado = []
    for letra in mensaje:
        if letra in homofonic_dict:
            sustituto = random.choice(homofonic_dict[letra])
            cifrado.append(str(sustituto))
    return '-'.join(cifrado)

def descifrar(cifrado):
    numeros = cifrado.split('-')
    descifrado = ''
    for num in numeros:
        descifrado += decrypt_dict.get(int(num), '?')
    return descifrado

# Ejemplo de uso
mensaje_original = "HOLA MUNDO"
cifrado = cifrar(mensaje_original)
descifrado = descifrar(cifrado)

print("Mensaje original:", mensaje_original)
print("Mensaje cifrado: ", cifrado)
print("Mensaje descifrado:", descifrado)
