from art import logo

alphabet = [
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o',
    'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'
]


def caesar(text, shift, direction):
    result_text = ""

    if direction == "decode":
        shift = shift * -1

    for letter in text:
        if letter in alphabet:
            position = alphabet.index(letter)
            new_position = (position + shift)

            if new_position > len(alphabet) - 1:
                new_position = new_position - len(alphabet)
            elif new_position < 0:
                new_position = new_position + len(alphabet)
            new_char = alphabet[new_position]
            result_text = result_text + new_char
        else:
            result_text = result_text + letter

    print(f"Here's the {direction}d result: {result_text}")
    restart = input(
        "Type 'yes' if you want to go again. Otherwise type 'no'.\n")
    if restart == "yes":
        cipher_program()
    else:
        print("Goodbye")

def cipher_program():
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    shift = shift % len(alphabet)
    caesar(text, shift, direction)


print(logo)
cipher_program()
