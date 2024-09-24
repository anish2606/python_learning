MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}
profit = 0
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

def is_resource_sufficient(order_ingridients):
    '''Return true when order can be made and return false if ingredients are insufficient.'''
    for item in order_ingridients:
        if order_ingridients[item] >= resources[item]:
            print(f"Sorry there is not enough {item}.")
            return False
    return True

def process_coins():
    '''Return the total calculated from the coins inserted.'''
    print("Please insert the coins")
    total = int(input("How many quarters?")) * 0.25
    total += int(input("How many quarters?")) * 0.1
    total += int(input("How many quarters?")) * 0.05
    total += int(input("How many quarters?")) * 0.01
    return total


def is_payment_succesful(money_recieved,drink_cost):
    '''Return true if payment is successful or false if money is insufficient'''
    if money_recieved > drink_cost:
        change = round(money_recieved - drink_cost, 2)
        print(f"Here is your ${change} in change.")
        global profit
        profit += drink_cost
        return True
    else:
        print("Insufficient money. Money refunded.")
        return False
    
def make_coffee(drink_name,order_ingredients):
    '''Deduct the required ingredients from the resources.'''
    for item in order_ingredients :
        resources[item] -= order_ingredients[item]
    print(f"Here is your coffee {drink_name}")

is_on = True

while is_on:
    choice = input("What coffee would you like? (espresso/latte/cappuccino): ")
    if choice ==  "off":
        is_on = False
    elif choice == "report":
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}ml")
        print(f"Money: {profit}")
    else:
        drink = MENU[choice]
        if is_resource_sufficient(drink["ingredients"]):
            payment = process_coins()
            if is_payment_succesful (payment , drink['cost']):
                make_coffee(choice , drink["ingredients"])

            
       
