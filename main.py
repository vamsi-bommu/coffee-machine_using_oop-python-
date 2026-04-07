from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine
from menu import MenuItem , Menu

moneymachine=MoneyMachine()
coffeemaker=CoffeeMaker()
menu=Menu()

k=True
while k:
    choice=input(f"What would you like? ({menu.get_items()}) : ")
    if choice=='off':
        k=False
    elif choice=='report':
        coffeemaker.report()
        moneymachine.report()
    elif choice in  ['espresso','latte','cappuccino']:
        drink=menu.find_drink(choice)
        if coffeemaker.is_resource_sufficient(drink):
           if  moneymachine.make_payment(drink.cost):
               coffeemaker.make_coffee(drink)
            
            