import random

# Crear un diccionario con letras del alfabeto y sus posibles sustituciones
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

# Función de cifrado por sustitución homofónica
def cifrar(texto):
    texto = texto.upper()
    texto_cifrado = []
    for char in texto:
        if char in alfabeto:
            sustituto = random.choice(sustituciones[char])  # Elegir un sustituto aleatorio
            texto_cifrado.append(sustituto)
        else:
            texto_cifrado.append(char)  # Dejar los caracteres no alfabéticos sin cambios
    return ''.join(texto_cifrado)

# Función de descifrado (solo para un descifrado simple)
def descifrar(texto_cifrado):
    # Invertir el diccionario para la búsqueda de los caracteres originales
    inverso_sustituciones = {}
    for letra, opciones in sustituciones.items():
        for sustituto in opciones:
            inverso_sustituciones[sustituto] = letra

    texto_descifrado = []
    for char in texto_cifrado:
        if char in inverso_sustituciones:
            texto_descifrado.append(inverso_sustituciones[char])
        else:
            texto_descifrado.append(char)  # Dejar los caracteres no alfabéticos sin cambios
    return ''.join(texto_descifrado)

# Ejemplo de uso
texto_original = "Hola Mundo"
texto_cifrado = cifrar(texto_original)
texto_descifrado = descifrar(texto_cifrado)

print("Texto Original:", texto_original)
print("Texto Cifrado:", texto_cifrado)
print("Texto Descifrado:", texto_descifrado)
