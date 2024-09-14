import random
word_list = ['camel','Ball','Bat','Cricket']
#Guessing a random word from the list
lives = 6
choosen_word = random.choice(word_list)
print(choosen_word)

#guess a letter

placeholder = ""
word_len = len(choosen_word)

for each_word in range(word_len):
    placeholder += "_"
print(placeholder)

#While loop to guess the letter again
game_over= False
correct_letter = []
while not game_over:
      guess = input("Which letter do you want to enter?: ")

      display = ""

      for letter in choosen_word:
        if letter == guess:
            display += letter
            correct_letter.append(guess)
        elif letter in correct_letter:
            display += letter
        else:
            display += "_"
        
      print(display)

      if guess not in choosen_word:
          lives -= 1
          if lives == 0:
              game_over = True
              print("Game Over!!")
    
      if "_" not in display:
        game_over = True
        print("You won!")

