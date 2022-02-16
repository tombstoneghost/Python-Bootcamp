# Imports
from art import logo
from os import system, name


# Clear Function
def clear():
    print(name)
    if name == 'nt':
        system('cls')
    else:
        system('clear')


# Bids Dictionary
bids = {}

# End of Bids
end_of_bid = False

print(logo)

def find_highest_bidder(bidding_record):
    highest_bid = 0

    for bidder in bidding_record:
        bid_amount = bidding_record[bidder]

        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder

    print(f"The winner is {winner} with a bid of ${highest_bid}")


while not end_of_bid:
    bidder_name = input("What is your name? ")
    bid_price = int(input("What is your bid? $"))

    bids[bidder_name] = bid_price

    should_continue = input("Are there any other bidders? Type 'yes' or 'no'.\n").lower()

    if should_continue == "yes":
        clear()
    elif should_continue == "no":
        clear()
        end_of_bid = True
        find_highest_bidder(bidding_record=bids)
        


