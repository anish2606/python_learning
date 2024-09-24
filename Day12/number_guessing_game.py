from random import randint

EASY_TURNS = 10
HARD_TURNS = 5
turns = 0

def check_answer(user_guess,correct_answer,turns):        
   if user_guess > correct_answer:
        print("The number is too high.Guess again.")
        return turns - 1
   elif user_guess < correct_answer:
        print("The number is too low. Guess again")
        return turns - 1
   elif user_guess == correct_answer:
        print ("The number guessed by you is correct")
        return turns

def check_difficulty():
    level = input("Choose the level 'easy' or 'hard': ")
    if level == "easy":
        return EASY_TURNS
    else:
        return HARD_TURNS
    
def game():   

    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100")
    answer = randint(1,100)

    turns = check_difficulty()

    guess = 0
    while guess != answer:
        print(f"You have {turns} remaining to guess.")

        number = int(input("Guess a number: "))
        turns = check_answer(number,answer,turns)
        if turns== 0:
            print("You have runout of guesses. You lose.")
            return

       
game()

      


  