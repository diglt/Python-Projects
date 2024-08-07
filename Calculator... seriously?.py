
EndRepeat = False


Number1 = int(input("What's the first number?: "))

while EndRepeat != True:
    print("+\n-\n*\n/")
    Operation = input("Pick an operation: ")
    Number2 = int(input("What's the next number?: "))


    def Calculate(X,Y):
        if Operation == "+":
            return X + Y
        elif Operation == "-":
            return X - Y
        elif Operation == "*":
            return X * Y
        elif Operation == "/":
            return X / Y

    CalcNumber = Calculate(Number1, Number2)
    print(f"{Number1} {Operation} {Number2} = {CalcNumber}")


    Repeat = str(input(f"Type 'y' to continue calculating with {Number1} or type 'n' to start a new calculation: ")).lower()

    if Repeat == "y":
        continue
    else:
        EndRepeat = True
