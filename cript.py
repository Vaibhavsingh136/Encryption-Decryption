from cryptography.fernet import Fernet
import os

def generate_key():
    key = Fernet.generate_key()
    with open("secret.key", "wb") as key_file:
        key_file.write(key)
    print("Key generated and saved to secret.key")

def load_key():
    if not os.path.exists("secret.key"):
        raise FileNotFoundError("Key file not found. Generate key first using generate_key()")
    return open("secret.key", "rb").read()

def encrypt_file(input_file, output_file):
    key = load_key()
    cipher = Fernet(key)

    with open(input_file, "rb") as file:
        file_data = file.read()

    encrypted_data = cipher.encrypt(file_data)

    with open(output_file, "wb") as file:
        file.write(encrypted_data)
    print(f"File '{input_file}' encrypted and saved to '{output_file}'.")

def decrypt_file(input_file, output_file):
    key = load_key()
    cipher = Fernet(key)

    with open(input_file, "rb") as file:
        encrypted_data = file.read()

    decrypted_data = cipher.decrypt(encrypted_data)

    with open(output_file, "wb") as file:
        file.write(decrypted_data)
    print(f"File '{input_file}' decrypted and saved to '{output_file}'.")

# Properly indented main block
if __name__ == "__main__":
    #encrypt_file("C:\\Users\\KIIT0001\\Desktop\\Chatbot\\WORK\\example.txt", "C:\\Users\\KIIT0001\\Desktop\\Chatbot\\WORK\\example_encrypted.txt")
    decrypt_file("C:\\Users\\KIIT0001\\Desktop\\Chatbot\\WORK\\example_encrypted.txt", "C:\\Users\\KIIT0001\\Desktop\\Chatbot\\WORK\\example_decrypted.txt")