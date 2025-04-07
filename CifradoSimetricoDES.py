from Crypto.Cipher import DES
from Crypto.Random import get_random_bytes
import random
import binascii

# Crear un diccionario con letras del alfabeto y sus posibles sustituciones (homofónicas)
alfabeto = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
sustituciones = {
    'A': ['F', 'J', 'M', 'P'],
    'B': ['R', 'H', 'Z'],
    'C': ['T', 'X', 'Y'],
    'D': ['W', 'V'],
    'E': ['S', 'U', 'Q'],
    'F': ['A', 'K', 'B'],
    'G': ['L', 'D'],
    'H': ['G', 'N', 'C'],
    'I': ['O', 'P'],
    'J': ['E', 'F', 'R'],
    'K': ['T', 'W'],
    'L': ['I', 'H'],
    'M': ['Z', 'B'],
    'N': ['M', 'J'],
    'O': ['U', 'N'],
    'P': ['Y', 'S'],
    'Q': ['A', 'Z'],
    'R': ['E', 'T', 'H'],
    'S': ['D', 'O'],
    'T': ['X', 'V'],
    'U': ['L', 'K'],
    'V': ['J', 'W'],
    'W': ['C', 'P'],
    'X': ['I', 'R'],
    'Y': ['F', 'G'],
    'Z': ['U', 'L']
}


# Función de cifrado DES
def cifrado_des(texto, clave):
    # Asegurarse de que el texto es un múltiplo de 8 caracteres
    while len(texto) % 8 != 0:
        texto += ' '  # Rellenar con espacios si es necesario

    # Crear el cifrador DES con la clave proporcionada
    cipher = DES.new(clave, DES.MODE_ECB)

    # Cifrar el texto
    texto_cifrado = cipher.encrypt(texto.encode('utf-8'))
    return binascii.hexlify(texto_cifrado).decode('utf-8')


# Función de sustitución homofónica
def sustitucion_homofonica(texto):
    texto = texto.upper()
    texto_cifrado = []
    for char in texto:
        if char in alfabeto:
            sustituto = random.choice(sustituciones[char])  # Elegir un sustituto aleatorio
            texto_cifrado.append(sustituto)
        else:
            texto_cifrado.append(char)  # Dejar los caracteres no alfabéticos sin cambios
    return ''.join(texto_cifrado)


# Función de cifrado homofónico DES (aplicar cifrado DES y sustitución homofónica)
def cifrado_homofonico_des(texto, clave):
    # Primero aplicamos DES
    texto_cifrado_des = cifrado_des(texto, clave)

    # Después aplicamos la sustitución homofónica
    texto_cifrado_final = sustitucion_homofonica(texto_cifrado_des)

    return texto_cifrado_final


# Función de descifrado (solo para un descifrado simple)
def descifrado_des(texto_cifrado, clave):
    # Eliminar la conversión hexadecimal
    texto_cifrado_bytes = binascii.unhexlify(texto_cifrado)

    # Crear el descifrador DES con la misma clave
    cipher = DES.new(clave, DES.MODE_ECB)

    # Descifrar el texto
    texto_descifrado = cipher.decrypt(texto_cifrado_bytes)
    return texto_descifrado.decode('utf-8').strip()  # Eliminar los espacios añadidos


# Ejemplo de uso
clave_des = get_random_bytes(8)  # Clave de 8 bytes (64 bits) para DES
texto_original = "Hola Mundo"

# Cifrado por homofónica DES
texto_cifrado = cifrado_homofonico_des(texto_original, clave_des)
texto_descifrado = descifrado_des(texto_cifrado, clave_des)

print("Texto Original:", texto_original)
print("Texto Cifrado:", texto_cifrado)
print("Texto Descifrado:", texto_descifrado)

