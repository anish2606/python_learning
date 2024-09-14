import random

print("Welcome to the 'Stone Paper Scissor' game!")

user_choice = int(input("what do you want to choose? Type 0 for Stone Type 1 for Paper and Type 2 for Scissor: "))

machine_choice = random.randint(0,2)
print(f"The computer chose {machine_choice}")

if user_choice>=3 or user_choice<0:
    print("You chose an invalid number ")

elif user_choice == 0 and machine_choice == 2 :
    print("User wins!")

elif machine_choice ==0 and user_choice == 2:
    print("Opponent wins!")

elif machine_choice > user_choice:
    print("Opponent won!")

elif user_choice > machine_choice:
    print ("you win!")

elif user_choice == machine_choice:
    print ("Its a draw")

