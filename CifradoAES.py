from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
import binascii

def cifrar_aes_ecb(texto, llave):
    llave_bytes = llave.encode('utf-8')
    if len(llave_bytes) != 16:
        raise ValueError("La llave debe tener exactamente 16 bytes (AES-128)")
    texto_bytes = texto.encode('utf-8')
    cipher = AES.new(llave_bytes, AES.MODE_ECB)
    texto_padded = pad(texto_bytes, AES.block_size)
    cifrado = cipher.encrypt(texto_padded)
    return binascii.hexlify(cifrado).decode('utf-8')

def descifrar_aes_ecb(texto_cifrado_hex, llave):
    llave_bytes = llave.encode('utf-8')
    if len(llave_bytes) != 16:
        raise ValueError("La llave debe tener exactamente 16 bytes (AES-128)")
    texto_cifrado = binascii.unhexlify(texto_cifrado_hex)
    cipher = AES.new(llave_bytes, AES.MODE_ECB)
    texto_descifrado_padded = cipher.decrypt(texto_cifrado)
    texto_descifrado = unpad(texto_descifrado_padded, AES.block_size)
    return texto_descifrado.decode('utf-8')

def menu():
    while True:
        print("\n--- AES-128 ECB ---")
        print("1. Cifrar texto")
        print("2. Descifrar texto")
        print("3. Salir")
        opcion = input("Selecciona una opción: ")

        if opcion == '1':
            texto = input("Introduce el texto a cifrar: ")
            llave = input("Introduce la llave (16 caracteres): ")
            try:
                resultado = cifrar_aes_ecb(texto, llave)
                print("Texto cifrado (hex):", resultado)
            except Exception as e:
                print("Error:", e)

        elif opcion == '2':
            texto_cifrado = input("Introduce el texto cifrado (hex): ")
            llave = input("Introduce la llave (16 caracteres): ")
            try:
                resultado = descifrar_aes_ecb(texto_cifrado, llave)
                print("Texto descifrado:", resultado)
            except Exception as e:
                print("Error:", e)

        elif opcion == '3':
            print("Saliendo...")
            break
        else:
            print("Opción no válida, intenta de nuevo.")

if __name__ == "__main__":
    menu()
