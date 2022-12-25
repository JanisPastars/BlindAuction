MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "milk": 0,
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
}


quarters = 0.25
dimes = 0.1
nickels = 0.05
pennies = 0.01


def choice_cost(you_choice, espresso_cost, latte_cost, cappuccino_cost):
    if you_choice == "e":
        return espresso_cost
    elif you_choice == "l":
        return latte_cost
    elif you_choice == "c":
        return cappuccino_cost


def get_ingredients(you_choice):
    if you_choice == "e":
        return "espresso"
    elif you_choice == "l":
        return "latte"
    elif you_choice == "c":
        return "cappuccino"


"""Get cost drink"""
espresso_cost = MENU["espresso"]["cost"]
latte_cost = MENU["latte"]["cost"]
cappuccino_cost = MENU["cappuccino"]["cost"]
print(f"Espresso {espresso_cost} $, Latte {latte_cost} $, Cappuccino  {cappuccino_cost} $")


w = resources["water"]
m = resources["milk"]
c = resources["coffee"]


def coffee_machine():
    money = 0
    water = w
    milk = m
    coffee = c
    one_more = True
    while one_more:
        you_choice = input("What would you like espresso/latte/cappuccino or report/off ").lower()
        drink = get_ingredients(you_choice)
        print(drink)
        if you_choice == "report":
            print(f"Water remained - {water}\nMilk remained - {milk}\nCoffee remained - {coffee}f\n"
                  f"Money in {money}")
        elif you_choice == "off":
            one_more = False
        elif you_choice != "e" and you_choice != "l" and you_choice != "c":
            print("Choice correct ")
        else:
            cost = choice_cost(you_choice, espresso_cost, latte_cost, cappuccino_cost)
            pcs_quarters = int(input("Insert quarters: "))
            pcs_dimes = int(input("Insert dimes: "))
            pcs_nickels = int(input("Insert nickels: "))
            pcs_pennies = int(input("Insert pennies: "))

            money_in = pcs_quarters * quarters + pcs_dimes * dimes + pcs_nickels * nickels + pcs_pennies * pennies
            money_back = money_in - cost

            if money_back < 0:
                print(f"Not enough money. You have puttied in: {money_in} $")
            else:
                water_for_drink = MENU[drink]["ingredients"]["water"]
                milk_for_drink = MENU[drink]["ingredients"]["milk"]
                coffee_for_drink = MENU[drink]["ingredients"]["coffee"]
                if water < water_for_drink or milk < milk_for_drink or coffee < coffee_for_drink:
                    print(f"Not enough ingredients.\n"
                          f"Water remained - {water}\nMilk remained - {milk}\nCoffee remained - {coffee}")
                    one_more = False
                else:
                    print(f"Here is your coffee. Money back: {money_back} $")
                    money += cost
                    water -= water_for_drink
                    milk -= milk_for_drink
                    coffee -= coffee_for_drink
                    print(f"Water remained - {water}\nMilk remained - {milk}\nCoffee remained - {coffee}\n"
                          f"Money in {money}")
    if input("One coffee ") == "y":
        coffee_machine()


coffee_machine()

