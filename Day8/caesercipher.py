alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt and 'decode' to decrypt:\n") .lower()
text = input("Type your message:\n") .lower()
shift = int(input("Type the shift number:\n"))

#Create a function called encrypt() that takes original_text and shift_amount as inputs 

#Inside the encrypt function shift each letter of the original_text forwards in the alphabet
#by the shift amount and prints the encrypted text.

def encrypt(original_text,shift_amount):
    cipher_text = ""

    for letter in original_text:
       shifted_position = alphabet.index(letter) + shift_amount
       shifted_position %= len(alphabet) #this is added bcz beyond z it should start from
                                            #start itself
       cipher_text += alphabet[shifted_position]

    print(cipher_text)

encrypt(original_text=text, shift_amount=shift)
    