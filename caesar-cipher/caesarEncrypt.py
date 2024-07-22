alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
from art import logo
print(logo)

should_continue = True

while should_continue:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    shift = shift % 26


    def caeser(direction_way, start_text, shift_amount):
        cipher_text = ""
        if direction_way == "decode":
            shift_amount *= -1
        for char in start_text:
            if char in alphabet:
                position = alphabet.index(char)
                new_position = position + shift_amount
                cipher_text += alphabet[new_position]
            else:
                cipher_text += char

        print(f"{direction} word is {cipher_text}")


    caeser(direction_way=direction, start_text=text, shift_amount=shift)
    result = input("If you want to do again type 'Yes' or type 'No' ")
    if result == "Yes":
        should_continue = True
    else:
        should_continue = False

