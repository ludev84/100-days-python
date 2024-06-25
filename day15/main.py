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
    "money": 0.0,
}


def process_coins():
    print("Please insert coins")
    quarters = int(input("how many quarters?: "))
    dimes = int(input("how many dimes?: "))
    nickels = int(input("how many nickels?: "))
    pennies = int(input("how many pennies?: "))
    total = quarters * 0.25 + dimes * 0.10 + nickels * 0.05 + pennies * 0.01
    total = round(total, 2)
    return total


def print_report():
    print(f'Water: {resources['water']}ml')
    print(f'Milk: {resources['milk']}ml')
    print(f'Coffee: {resources['coffee']}g')
    print(f'Money: ${round(resources['money'], 2)}')


def check_resources(item):
    for key in item['ingredients']:
        if item['ingredients'][key] > resources[key]:
            return key
    return True


def process_beverage(money, item, item_name):
    change = money - item['cost']
    resources['money'] += money - change
    for key in item['ingredients']:
        resources[key] -= item['ingredients'][key]
    print(f"Here is ${change} in change")
    print(f"Here is your {item_name} ☕. Enjoy!")


while True:
    selection = input("What would you like? (espresso/latte/cappuccino): ").lower()

    if selection == 'off':
        exit()
    elif selection == 'report':
        print_report()
    else:
        selected_item = MENU[selection]
        enough_resources = check_resources(selected_item)
        if isinstance(enough_resources, str):
            print(f"Sorry, there's not enough {enough_resources}")
        else:
            payment = process_coins()
            if payment < selected_item['cost']:
                print("Sorry that's not enough money. Money refunded.")
            else:
                process_beverage(payment, selected_item, selection)
