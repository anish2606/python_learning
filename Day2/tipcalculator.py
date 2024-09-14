print("Welcome to the tip calculator!!")

bill = int(input("What was the total bill?: $"))
tip = int(input("How much tip you are going to give? 10,12 or 15 : "))
people = int(input("How many people share the bill? "))

bill_with_tip = tip/100 * bill + bill

result = ((bill + bill_with_tip)/people)

total = print(f"Each person should pay ${result}")