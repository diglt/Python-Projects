import DataStorage

MachineGoods = DataStorage.StartingResources
CoffeTypes = DataStorage.Coffees
Currency = DataStorage.Currency
IsRunning = True


def ReturnMachineGoods():
    for Index, Value in MachineGoods.items():
        print(Index, Value)


def ReturnCoffeeValue(coffee, value):
    CoffeeInDict = CoffeTypes[coffee]
    for _, skibidi in CoffeeInDict.items():
        if _ == value:
            return skibidi


def ReturnTotalAmount(Item):
    for a, price in Currency.items():
        if a == Item:
            return price


def AddMoney(amount):
    for Index, Value in MachineGoods.items():
        if Index == "Money":
            Value += amount


def RemoveResources(water, milk, coffee, money):
    for Index, Value in MachineGoods.items():
        if Index == "Water":
            MachineGoods[Index] -= water
        elif Index == "Milk":
            MachineGoods[Index] -= milk
        elif Index == "Coffee":
            MachineGoods[Index] -= coffee
        elif Index == "Money":
            MachineGoods[Index] += money


def CheckEnoughRescources(ItemWater, ItemMilk, ItemCoffee):
    for a, b in MachineGoods.items():
        if a == "Water" and b < ItemWater:
            return False
        if a == "Milk" and b < ItemMilk:
            return False
        if a == "Coffee" and b < ItemCoffee:
            return False
        else:
            return True


while IsRunning:
    Choice = str(input(f"What would you like? (espresso/latte/cappuccino): ")).lower()

    if Choice == "report":
        ReturnMachineGoods()

    if Choice == "off":
        IsRunning = False

    elif Choice != "report" and Choice != "off":
        Price = ReturnCoffeeValue(Choice, "Price")
        Water = ReturnCoffeeValue(Choice, "Water")
        Coffee = ReturnCoffeeValue(Choice, "Coffee")
        Milk = ReturnCoffeeValue(Choice, "Milk")
        Total = CheckEnoughRescources(Water, Coffee, Milk)

        print("Please insert coins.")

        Quaters = int(input("How many quaters?: ")) * ReturnTotalAmount("Quater")
        Dimes = int(input("How many dimes?: ")) * ReturnTotalAmount("Dime")
        Nickels = int(input("How many nickels?: ")) * ReturnTotalAmount("Nickel")
        Pennies = int(input("How many pennies: ")) * ReturnTotalAmount("Penny")

        AmountPaid = Quaters + Dimes + Nickels + Pennies

        if AmountPaid < Price:
            print("You didn't pay enough. Sadly no coffee for you :(")
            IsRunning = False

        elif AmountPaid >= Price and Total:
            RemoveResources(Water, Coffee, Milk, Price)

            Change = round(AmountPaid - Price, 2)
            print(f"Here's your coffee ☕ \nYour change is {Change}")

        elif AmountPaid > Price and not Total:
            print("Sorry the machine is out of materials :(")
            IsRunning = False
