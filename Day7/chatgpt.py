import random

word_list = ['camel', 'Ball', 'Bat', 'Cricket']
# Choosing a random word from the list
chosen_word = random.choice(word_list).lower()  # Convert to lowercase for case-insensitive comparison
print(chosen_word)  # Optional: You can remove this line if you don't want to show the chosen word

# Placeholder for guessed letters
placeholder = "_" * len(chosen_word)
print(placeholder)

# While loop to guess the letter again
game_over = False
while not game_over:
    guess = input("Which letter do you want to enter?: ").lower()  # Convert input to lowercase

    new_placeholder = ""
    for i in range(len(chosen_word)):
        if chosen_word[i] == guess:
            new_placeholder += guess
        else:
            new_placeholder += placeholder[i]  # Preserve already guessed letters

    placeholder = new_placeholder
    print(placeholder)

    if "_" not in placeholder:
        game_over = True
        print("You won!")
