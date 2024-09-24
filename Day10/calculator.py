def add (n1,n2):
    return n1+n2

def sub (n1,n2):
    return n1-n2

def mul (n1,n2):
    return n1*n2

def div (n1,n2):
    return n1/n2

operations = {
    "+" :add ,
    "-" :sub ,
    "*" :mul ,
    "/" : div
}
def calculator():

    num1 = float(input("Enter the 1st number: "))
    should_accumulate = True
    while should_accumulate:
        
        for symbol in operations:
            print(symbol)

        operator = input("Choose an operation: ")
        num2 = float(input("Enter the 2nd number: "))
        answer = (operations[operator](num1,num2))
        print(f"{num1} {operator} {num2}= {answer}")
        
        choice = input(f"Type 'y'to continue with the {answer} or type 'n' to continue with the new number: ")
        if choice == "y":
            num1 = answer   
        elif choice == "n":
            print("\n"*15)
            calculator()

calculator()

