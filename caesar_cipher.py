from string import ascii_lowercase


alphabet = list(ascii_lowercase)


def caesar_cipher_encrypt(plain_text: str, shift_number: int) -> str:
    global alphabet
    cipher_text = ""
    for letter in plain_text:
        position = alphabet.index(letter)
        new_position = (position + shift_number) % 26
        new_letter = alphabet[new_position]
        cipher_text += new_letter

    return cipher_text


def caesar_cipher_decrypt(cipher_text: str, shift_number: int):
    global alphabet
    plain_text = ""
    for letter in cipher_text:
        position = alphabet.index(letter)
        new_position = (position - shift_number) % 26
        plain_text += alphabet[new_position]

    return plain_text


def main():
    number = 2
    while number > 0:
        direction = input("Type 'encode' to encrypt, type 'decode' to decrypt: ")
        if direction == "encode":
            text = input("Type your message: ").lower()
            shift = int(input("Type your shift number: "))
            cipher_text = caesar_cipher_encrypt(plain_text=text, shift_number=shift)
            print("The encoded text is", cipher_text)
            number -= 1
        elif direction == "decode":
            text = input("Enter the message to decrypt: ").lower()
            shift = int(input("Type your shift number: "))
            plain_text = caesar_cipher_decrypt(cipher_text=text, shift_number=shift)
            print("The decoded text is", plain_text)
            number -= 1
        else:
            print("Enter a valid input!!!")


if __name__ == "__main__":
    main()
