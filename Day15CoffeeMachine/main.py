from database import MENU, resources


def show_report():
    for key in resources:
        if key == "water" or key == "milk":
            print(f"{key.capitalize()}: {resources[key]}ml")
        elif key == "coffee":
            print(f"{key.capitalize()}: {resources[key]}g")
        elif key == "profit":
            print(f"{key.capitalize()}: ${resources[key]}")


def enough_resources(menu_item):
    """Returns True if there are enough resources, otherwise False"""
    is_enough = True
    """Returns TRUE if there are enough resources. If not, it will print what is missing"""
    for ingredient in MENU[menu_item]["ingredients"]:
        if MENU[menu_item]["ingredients"][ingredient] > resources[ingredient]:
            print(f"Sorry there is not enough {ingredient}.")
            is_enough = False
    if not is_enough:
        # I'm doing this so that it will display all missing resources
        # instead of returning from the function immediately
        return
    return True


def process_coins():
    """Returns the total value of inserted coins."""
    print("Please insert coins.")
    quarters = int(input("how many quarters?: "))
    dimes = int(input("how many dimes?: "))
    nickles = int(input("how many nickles?: "))
    pennies = int(input("how many pennies?: "))
    return round(quarters * 0.25 + dimes * 0.10 + nickles * 0.05 + pennies * 0.01, 2)


def process_transaction(inserted_money, chosen_product):
    """Returns true if it's enough money, otherwise prints an error."""
    product_cost = MENU[chosen_product]["cost"]
    if inserted_money < product_cost:
        print("Sorry that's not enough money. Money refunded.")
    else:
        if inserted_money == product_cost:
            resources["profit"] += inserted_money
            return True
        elif inserted_money > product_cost:
            change = round(inserted_money - product_cost, 2)
            resources["profit"] += (inserted_money - change)
            print(f"Here is ${change} in change.")
            return True


def make_coffee(dispense_product):
    # Since I am using "MENU[dispense_product]["ingredients"]" twice, I could just pass this to this function instead
    for ingredient in MENU[dispense_product]["ingredients"]:
        resources[ingredient] -= MENU[dispense_product]["ingredients"][ingredient]
    print(f"Here is your {dispense_product.capitalize()}. Enjoy! ☕️")


while True:
    product = input("What would you like? (espresso/latte/cappuccino): ").lower()
    if product == "report":
        show_report()
    elif product == "off":
        exit()
    else:
        if enough_resources(product):
            print(f"The {product.capitalize()} is ${MENU[product]['cost']}")
            total_coin_value = process_coins()
            if process_transaction(total_coin_value, product):
                make_coffee(product)
