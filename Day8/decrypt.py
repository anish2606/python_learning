alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt and 'decode' to decrypt:\n") .lower()
text = input("Type your message:\n") .lower()
shift = int(input("Type the shift number:\n"))


def decrypt(original_text,shift_amount):
    output_text = ""

    for letter in original_text:
        shifted_position = alphabet.index(letter) - shift_amount
        shifted_position %= len(alphabet)
        output_text += alphabet[shifted_position]
    
    print (output_text)

decrypt(original_text=text, shift_amount=shift)


