def highest_bid(bid_dictionary):
    winner = ""
    highest_bid = 0
    for name in bid_dictionary:
        amount = bid_dictionary[name]
        if amount > highest_bid:
            highest_bid = amount
            winner = name
    
    print(f"The winner is {winner} with a bid of ${highest_bid}")

continue_bid = True
while continue_bid:
    print ("Welcome to the Secret Auction ")
    name = input("Enter the name of the person: ")
    amount = int(input("Enter the amount of the bid: $"))
    bid = {}
    bid[name] = amount
    re_bid = input("Do you want others do bid again? Type 'Y'for Yes and 'N' for No: ").lower()
    if re_bid == "n":
        continue_bid = False
        highest_bid(bid)
    elif re_bid == "y":
        print("\n"* 20)


