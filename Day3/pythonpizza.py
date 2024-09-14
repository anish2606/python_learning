print("Welcome to the Python Pizza Deliveries !")

size = input("What size pizza do you want? S, M or L: ")
pepperoni =  input("Do you want pepperoni on your pizza? Y or N: ")
extra_cheese = input("Do you want extra cheese for your pizza? Y or N: ")

bill = 0
if size=="S":
    bill = 15

elif size=="M":
    bill = 20

elif size=="L":
    bill= 25

else:
    print("You have typed wrong inputs")

#pepperoni

if pepperoni=="Y":
    if size == "S":
        bill+=2
       
    else:
        bill+=3
       

#extra_cheese
if extra_cheese == "Y":
    bill+=1
    

final_bill= print(f"You final bill is: ${bill}")

