print('''Welcome to the treasure island.
      Your mission is to find the treasure''')

way = input ("You are the cross of road. Which way you want to go? Type left or right  ")

if way == "left":
    choice1= input('''You have come to a lake.There is an island in the middle of the lake
          Type "wait" to wait for a boat. Type "swim" to swim across  ''')
    if choice1== "wait":
        choice2= input('''You arrive at a island unharmed. There is a house with 3 doors. 
              One "red" , One "yellow", One "blue". Which one do you choose? ''')
        if choice2== "red":
            print("You have went a wrong way. Game Over!!")
        elif choice2== "blue":
            print ("You have entered into a hole. Game Over!!")
        elif choice2== "yellow":
            print("You have found the treasure You won! ")
        else:
            print("You entered the wrong color. Please enter the correct color.")
    elif "swim"== True:
        print("You are attacked by a shark. You lost!")
    else:
        print("Please choose either swim or wait!")
elif way == "right":
    print("You have entered into a hole. Game over!!!")
else:
    print("Please choose correct way")
