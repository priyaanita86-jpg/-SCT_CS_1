# Caesar Cipher Program
# Author: Priya
# Description: Encrypt and decrypt text using Caesar Cipher Algorithm.

def encrypt(text, shift):
    encrypted_text = ""

    for char in text:
        if char.isalpha():
            if char.isupper():
                encrypted_text += chr((ord(char) - ord('A') + shift) % 26 + ord('A'))
            else:
                encrypted_text += chr((ord(char) - ord('a') + shift) % 26 + ord('a'))
        else:
            encrypted_text += char

    return encrypted_text


def decrypt(text, shift):
    decrypted_text = ""

    for char in text:
        if char.isalpha():
            if char.isupper():
                decrypted_text += chr((ord(char) - ord('A') - shift) % 26 + ord('A'))
            else:
                decrypted_text += chr((ord(char) - ord('a') - shift) % 26 + ord('a'))
        else:
            decrypted_text += char

    return decrypted_text


def main():
    print("\n===== Caesar Cipher Program =====")

    while True:
        print("\n1. Encrypt")
        print("2. Decrypt")
        print("3. Exit")

        choice = input("Enter your choice (1-3): ")

        if choice == '1':
            text = input("Enter message to encrypt: ")
            shift = int(input("Enter shift value: "))

            encrypted = encrypt(text, shift)
            print("\nEncrypted Message:", encrypted)

        elif choice == '2':
            text = input("Enter message to decrypt: ")
            shift = int(input("Enter shift value: "))

            decrypted = decrypt(text, shift)
            print("\nDecrypted Message:", decrypted)

        elif choice == '3':
            print("Thank you for using Caesar Cipher!")
            break

        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()




