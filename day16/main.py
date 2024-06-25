from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menu = Menu()
coffeeMaker = CoffeeMaker()
moneyMachine = MoneyMachine()

while True:
  choice = input(f"What would you like? ({menu.get_items()}): ")
  if choice == 'off':
    exit()
  elif choice == 'report':
    coffeeMaker.report()
    moneyMachine.report()
  else:
    drink = menu.find_drink(choice)
    if coffeeMaker.is_resource_sufficient(drink):
      payment = moneyMachine.make_payment(drink.cost)
      if payment:
        coffeeMaker.make_coffee(drink)