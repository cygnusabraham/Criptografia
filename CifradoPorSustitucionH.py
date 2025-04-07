import random
import string

# Función que calcula el módulo de exponentes grandes
def mod_exp(base, exp, mod):
    return pow(base, exp, mod)

# Intercambio de claves Diffie-Hellman
def diffie_hellman(p, g):
    # Alice y Bob eligen números secretos aleatorios
    a = random.randint(1, p-1)
    b = random.randint(1, p-1)

    # Calculan sus claves públicas
    A = mod_exp(g, a, p)
    B = mod_exp(g, b, p)

    # Intercambian sus claves públicas
    K_a = mod_exp(B, a, p)  # Alice calcula la clave compartida
    K_b = mod_exp(A, b, p)  # Bob calcula la clave compartida

    return K_a  # La clave compartida debe ser igual para ambos

# Cifrado por sustitución homofónica
def homophonic_substitution_cipher(text, key):
    # Definir una tabla de sustitución homofónica (para simplificación)
    substitution_table = {
        'a': ['1', '2', '3'],
        'b': ['4', '5', '6'],
        'c': ['7', '8', '9'],
        'd': ['10', '11', '12'],
        'e': ['13', '14', '15'],
        'f': ['16', '17', '18'],
        'g': ['19', '20', '21'],
        'h': ['22', '23', '24'],
        'i': ['25', '26', '27'],
        'j': ['28', '29', '30'],
        'k': ['31', '32', '33'],
        'l': ['34', '35', '36'],
        'm': ['37', '38', '39'],
        'n': ['40', '41', '42'],
        'o': ['43', '44', '45'],
        'p': ['46', '47', '48'],
        'q': ['49', '50', '51'],
        'r': ['52', '53', '54'],
        's': ['55', '56', '57'],
        't': ['58', '59', '60'],
        'u': ['61', '62', '63'],
        'v': ['64', '65', '66'],
        'w': ['67', '68', '69'],
        'x': ['70', '71', '72'],
        'y': ['73', '74', '75'],
        'z': ['76', '77', '78'],
        ' ': ['79', '80', '81']  # Espacio también tiene varias representaciones
    }

    encrypted_text = ''
    for char in text.lower():
        if char in substitution_table:
            # Usamos la clave generada por Diffie-Hellman para seleccionar el índice
            options = substitution_table[char]
            # El índice se determina usando la clave, en este caso se usa un módulo de la longitud de opciones
            index = (key % len(options))
            encrypted_text += options[index] + ' '
        else:
            encrypted_text += char + ' '  # Si el caracter no está en la tabla, no lo cifra

    return encrypted_text.strip()

# Parámetros públicos de Diffie-Hellman
p = 23  # Número primo
g = 5   # Generador (base)

# Paso 1: Intercambio de claves Diffie-Hellman
shared_key = diffie_hellman(p, g)
print(f"Clave compartida generada por Diffie-Hellman: {shared_key}")

# Paso 2: Cifrado por sustitución homofónica con la clave compartida
text_to_encrypt = "hola mundo"
encrypted_text = homophonic_substitution_cipher(text_to_encrypt, shared_key)
print(f"Texto cifrado: {encrypted_text}")
