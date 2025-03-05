import random

class HomophonicCipher:
    def __init__(self):
        self.alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        self.mapping = {
            "A": ["11", "12", "13"], "B": ["21", "22"], "C": ["31", "32"], "D": ["41", "42"],
            "E": ["51", "52", "53", "54"], "F": ["61", "62"], "G": ["71", "72"], "H": ["81", "82"],
            "I": ["91", "92", "93"], "J": ["101"], "K": ["111"], "L": ["121", "122"],
            "M": ["131", "132"], "N": ["141", "142"], "O": ["151", "152"], "P": ["161", "162"],
            "Q": ["171"], "R": ["181", "182"], "S": ["191", "192"], "T": ["201", "202"],
            "U": ["211", "212"], "V": ["221"], "W": ["231"], "X": ["241"], "Y": ["251"], "Z": ["261"]
        }
        self.reverse_mapping = {v: k for k, values in self.mapping.items() for v in values}

    def encrypt(self, text):
        text = text.upper()
        encrypted_text = ""
        for char in text:
            if char in self.mapping:
                encrypted_text += random.choice(self.mapping[char]) + " "
            else:
                encrypted_text += char + " "
        return encrypted_text.strip()

    def decrypt(self, text):
        words = text.split()
        decrypted_text = ""
        for word in words:
            if word in self.reverse_mapping:
                decrypted_text += self.reverse_mapping[word]
            else:
                decrypted_text += word
        return decrypted_text

cipher = HomophonicCipher()
text = input("Ingrese el texto a cifrar: ")
ciphered = cipher.encrypt(text)
decrypted = cipher.decrypt(ciphered)

print(f"Texto original: {text}")
print(f"Texto cifrado: {ciphered}")
print(f"Texto descifrado: {decrypted}")
