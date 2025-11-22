"""
File Encryption & Decryption Tool
We use the Fernet encryption module from the `cryptography` library
to encrypt and decrypt files. It will allow the user to:

1. Generate a new encryption key (stored as key.key)
2. Load the existing encryption key
3. Encrypt a specified file
4. Decrypt a specified file

The encrypted data replaces the original file contents.
"""
from cryptography.fernet import Fernet


def generate_key():
    """
    Generates a new symmetric encryption key and saves it
    into a file named 'key.key'. Run this ONCE before
    encrypting or decrypting files.
    """
    key = Fernet.generate_key()
    with open("key.key", "wb") as key_file:
        key_file.write(key)
    print("New encryption key generated and saved as key.key")


def load_key():
    """
    Loads the encryption key from the key.key file.
    This key must have been created earlier using generate_key().
    """
    with open("key.key", "rb") as key_file:
        return key_file.read()

# Encryption and Decryption funcctions;

def encrypt_file(file_path, key):
    """
    Encrypts a file using the provided Fernet key.

    The encrypted data overwrites the original file content.
    """
    cipher = Fernet(key)

    # Read original data
    with open(file_path, "rb") as file:
        file_data = file.read()

    # Encrypt the data
    encrypted_data = cipher.encrypt(file_data)

    # Overwrite file with encrypted version
    with open(file_path, "wb") as file:
        file.write(encrypted_data)

    print(f"File '{file_path}' encrypted successfully!")


def decrypt_file(file_path, key):
    """
    Decrypts a file using the provided Fernet key.

    The decrypted data overwrites the encrypted content.
    """
    cipher = Fernet(key)

    with open(file_path, "rb") as file:
        encrypted_data = file.read()

    decrypted_data = cipher.decrypt(encrypted_data)

    with open(file_path, "wb") as file:
        file.write(decrypted_data)

    print(f"File '{file_path}' decrypted successfully!")


def main():
    """
    Main interactive menu for choosing encryption actions.
    This prevents automatic encrypt/decrypt when importing the file.
    """

    print("\n--- FILE ENCRYPTION TOOL ---")
    print("1. Generate a new key")
    print("2. Encrypt a file")
    print("3. Decrypt a file")
    print("4. Exit")

    choice = input("Select an option: ")

    if choice == "1":
        generate_key()

    elif choice == "2":
        key = load_key()
        file_path = input("Enter the file name to encrypt: ")
        encrypt_file(file_path, key)

    elif choice == "3":
        key = load_key()
        file_path = input("Enter the file name to decrypt: ")
        decrypt_file(file_path, key)

    elif choice == "4":
        print("Exiting...")
        return
    else:
        print("Invalid choice. Please try again.")


if __name__ == "__main__":
    # Ensures the interactive menu only runs when executing main.py directly
    main()

