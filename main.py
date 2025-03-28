#program to do a simple encryption and decryption
import string
import random

chars = string.ascii_letters + string.punctuation + string.digits + " "
chars = list(chars)
key = chars.copy()
random.shuffle(key)

def encrypt(text):
    cipher_text = ""
    for letter in text:
        index = chars.index(letter)
        # append is a list method
        cipher_text += key[index]
    print(f"Encrypted message: {cipher_text}")
    return cipher_text

def decrypt(text):
    decrypted_message = ""
    for letter in text:
        index = key.index(letter)
        decrypted_message += chars[index]
    print(f"decrypted message: {decrypted_message}")


plaintext = input ("Enter a message to encrypt: ")
encrypted_text = encrypt(plaintext)
decrypt(encrypted_text)
