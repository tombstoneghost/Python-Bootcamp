# Menu
from re import T
from tokenize import cookie_re


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

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
    "money": 0
}

# Machine State
off = False

def report():
    print(f'Water: {resources["water"]}ml')
    print(f'Milk: {resources["milk"]}ml')
    print(f'Coffee: {resources["coffee"]}g')
    print(f'Money: ${resources["money"]}')

def is_sufficient(coffee):
    if resources["water"] < MENU[coffee]["ingredients"]["water"]:
        print("Sorry there is not enough water.")
        return False
    if resources["coffee"] < MENU[coffee]["ingredients"]["coffee"]:
        print("Sorry there is not enough coffee.")
        return False
    
    if coffee != "espresso":
        if resources["milk"] < MENU[coffee]["ingredients"]["milk"]:
            print("Sorry there is not enough milk.")
            return False

    return True

def process_coins(quaters, dimes, nickels, pennies):
    total_quaters = quaters * 0.25
    total_dimes = dimes * 0.10
    total_nickles = nickels * 0.05
    total_pennies = pennies * 0.01

    total_amount = total_quaters + total_dimes + total_nickles + total_pennies

    return total_amount

def make_coffee(coffee):
    resources["water"] = resources["water"] - MENU[coffee]["ingredients"]["water"]
    resources["coffee"] = resources["coffee"] - MENU[coffee]["ingredients"]["coffee"]

    if coffee != "espresso":
        resources["milk"] = resources["milk"] - MENU[coffee]["ingredients"]["milk"]

while not off:
    prompt = input("What would you like? (espresso/latte/cappuccino): ").lower()

    if prompt == "off":
        off = True
    elif prompt == "report":
        report()
    elif prompt in MENU.keys():
        if not is_sufficient(prompt):
            off = True
        else:
            print("Please Insert Coins")
            quaters = int(input("How many quaters?: "))
            dimes = int(input("How many dimes?: "))
            nickles = int(input("How many nickles?: "))
            pennies = int(input("How many pennies?: "))

            amount_given = process_coins(quaters, dimes, nickles, pennies)

            if amount_given < MENU[prompt]["cost"]:
                print("Sorry, that's not enough money. Money refunded.")
            else:
                change = amount_given - MENU[prompt]["cost"]
                resources['money'] = resources['money'] + MENU[prompt]["cost"]

                if change > 0:
                    print("Here is ${:.2f} in change.".format(change))
                make_coffee(prompt)

                print(f"Here is your {prompt}. Enjoy!")
    



