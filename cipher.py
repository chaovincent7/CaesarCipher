def caesar_decrypt(ciphertext, shift):
    plaintext = ""
    for c in ciphertext:
        if c.isalpha():
            plaintext += chr((ord(c) - shift - 65) % 26 + 65)
        else:
            plaintext += c
    return plaintext


ciphertext = input("Enter the ciphertext to decrypt: ")
shift = int(input("Enter the shift value used in the encryption: "))

plaintext = caesar_decrypt(ciphertext, shift)

print("Decrypted plaintext:", plaintext)
