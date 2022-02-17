# Imports
from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

# Machine State
off = False

# Objects
menu = Menu()
coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()

while not off:
    options = menu.get_items()

    prompt = input(f"What would you like? ({options}): ").lower()

    if prompt == "off":
        off = True
    elif prompt == "report":
        coffee_maker.report()
        money_machine.report()
    else:
        coffee_type = menu.find_drink(prompt)

        if coffee_maker.is_resource_sufficient(coffee_type) and money_machine.make_payment(coffee_type.cost):
            coffee_maker.make_coffee(coffee_type)



