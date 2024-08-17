from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine
from prettytable import prettytable

table = prettytable.PrettyTable()
table.add_column("Choices", ["coffee", "report", "off"])

CoffeeMaker = CoffeeMaker()
Menu = Menu()
MoneyMachine = MoneyMachine()

IsRunning = True

while IsRunning:
    InputtedChoice = str(input(f"Welcome to the coffee machine!"
                               "What would you like to do?\n"
                               f"{table}\n"
                               )).upper()

    if InputtedChoice == "REPORT":
        CoffeeMaker.report()
        MoneyMachine.report()

    if InputtedChoice == "OFF":
        print("\nUnderstood, Coffe machine is now disabled.")
        IsRunning = False

    elif InputtedChoice == "COFFEE":
        Choice = str(input("\nWhat coffe would you like?\nespresso\nlatte\ncappuccino?\n")).lower()
        IsInMenu = Menu.find_drink(Choice)

        if not IsInMenu:
            print('Sorry that drink is not available.\n')
        else:
            Rescourses = CoffeeMaker.is_resource_sufficient(IsInMenu)

            if Rescourses:
                SuccessOrNot = MoneyMachine.make_payment(IsInMenu.cost)

                if SuccessOrNot:
                    CoffeeMaker.make_coffee(IsInMenu)
                    GoAgain = str(input("Would you like to go again?\n")).upper()

                    if GoAgain[0] == "Y":
                        for a in range(1, 10):
                            print("\n")
                        continue
                    else:
                        IsRunning = False
