import math

def add():
    quantity = int(input("How many numbers would you like to add on? "))
    if quantity > 0:
        first=float(input("Please enter the original number to add to: "))
        second=float(input("Please enter the first number to add on: "))
        first = first + second
        for i in range(quantity-1):
            second=float(input("Please enter the next number to add on: "))
            first = first + second
        return(first)
    else:
        print("Your input was not valid.")
        add()

def subtract():
    quantity = int(input("How many numbers would you like to subtract by? "))
    if quantity > 0:
        first=float(input("Please enter the original number to subtract from: "))
        second=float(input("Please enter the first number to subtract by: "))
        first = first - second
        for i in range(quantity-1):
            second=float(input("Please enter the next number to subtract by: "))
            first = first - second
        return(first)
    else:
        print("Your input was not valid.")
        subtract()

def multiply():
    quantity = int(input("How many numbers would you like to multiply by? "))
    if quantity > 0:
        first=float(input("Please enter the original number to multiply from: "))
        second=float(input("Please enter the first number to multiply by: "))
        first = first * second
        for i in range(quantity-1):
            second=float(input("Please enter the next number to multiply by: "))
            first = first * second
        return(first)
    else:
        print("Your input was not valid.")
        multiply()

def divide():
    quantity = int(input("How many numbers would you like to divide the original number by? "))
    if quantity > 0:
        first=float(input("Please enter the original number to divide from: "))
        second=float(input("Please enter the first number to divide by: "))
        first = first / second
        for i in range(quantity-1):
            second=float(input("Please enter the next number to divide by: "))
            first = first / second
        return(first)
    else:
        print("Your input was not valid.")
        divide()

def square():
    first=float(input("Please enter the original number to square: "))
    first = first * first
    return(first)

def perimeter():
    quantity = int(input("How many sides does the shape have? "))
    if quantity > 0:
        first=float(input("Please enter the first length: "))
        for i in range(quantity-1):
            second=float(input("Please enter the next length: "))
            first = first + second
        return(first)
    else:
        print("Your input was not valid.")
        perimeter()

def circumference():
    first=float(input("Please enter the radius of your circle: "))
    first = 2 * math.pi * first
    return(first)

def modulus():
    first=float(input("Please enter the original number to use modulus on: "))
    second=float(input("Please enter the number to apply modulus by: "))
    first = first % second
    return(first)

def floordivision():
    first=float(input("Please enter the original number to floor divide from: "))
    second=float(input("Please enter the number to floor divide by: "))
    first = first % second
    first = int(first)
    return(first)

def exponentiation():
    first=float(input("Please enter the original number to exponentiate: "))
    second=float(input("Please enter the power to exponentiate by: "))
    first = first ** second
    return(first)
        
def menu():
        choice=input("Please enter an option: ")
        check = choice.isnumeric()
        while check == False:
            print("Your input was not valid.")
            choice=input("Please enter an option: ")
            check = choice.isnumeric()
        chosen = False
        while chosen == False:
            if int(choice) == 1:
                print("You have chosen to add.")
                chosen = True
                return choice
            elif int(choice) == 2:
                print("You have chosen to subtract.")
                chosen = True
                return choice
            elif int(choice) == 3:
                print("You have chosen to multiply.")
                chosen = True
                return choice
            elif int(choice) == 4:
                print("You have chosen to divide.")
                chosen = True
                return choice
            elif int(choice) == 5:
                print("You have chosen to square.")
                chosen = True
                return choice
                break
            elif int(choice) == 6:
                print("You have chosen to find the perimeter.")
                chosen = True
                return choice
            elif int(choice) == 7:
                print("You have chosen to find the circumference.")
                chosen = True
                return choice
            elif int(choice) == 8:
                print("You have chosen to use modulus.")
                chosen = True
                return choice
            elif int(choice) == 9:
                print("You have chosen to floor divide.")
                chosen = True
                return choice
            elif int(choice) == 10:
                print("You have chosen to exponentiate.")
                chosen = True
                return choice
            else:
                print("Your input was not valid.")
                choice=input("Please enter an option: ")
                check = choice.isnumeric()
                while check == False:
                    print("Your input was not valid.")
                    choice=input("Please enter an option: ")
                    check = choice.isnumeric()

def result():
    global count
    count = input("Welcome to Simple Calcultor\n----------------------\nHow many times would you like to use the calculator? ")
    check = count.isnumeric()
    if count == '0':
            print("Goodbye.")
            exit()
    while check == False:
        if count == 0:
            check == True
        print("Your input was not valid.")
        count=input("Please enter an option: ")
        if count == '0':
            print("Goodbye.")
            exit()
        check = count.isnumeric()
    count = int(count)
    for i in range(count):
        print("This is operation",i+1,"out of",str(count)+".")
        print("[1] to add")
        print("[2] to subtract")
        print("[3] to multiply")
        print("[4] to divide")
        print("[5] to square")
        print("[6] to find the perimeter")
        print("[7] to find the circumference")
        print("[8] to use modulus")
        print("[9] to floor divide")
        print("[10] to exponentiate")
        choice = int(menu())
        if int(choice) == 1:
            result = add()
            print("The result of your addition is",str(result)+".") 
        elif int(choice) == 2:
            result = subtract()
            print("The result of your subtraction is",str(result)+".") 
        elif int(choice) == 3:
            result = multiply()
            print("The result of your multiplication is",str(result)+".") 
        elif int(choice) == 4:
            result = divide()
            print("The result of your division is",str(result)+".")
        elif int(choice) == 5:
            result = square()
            print("The result of your square is",str(result)+".")
        elif int(choice) == 6:
            result = perimeter()
            print("The result of your perimeter is",str(result)+".")
        elif int(choice) == 7:
            result = circumference()
            print("The result of your circumference is",str(result)+".")
        elif int(choice) == 8:
            result = modulus()
            print("The result of your modulus is",str(result)+".")
        elif int(choice) == 9:
            result = floordivision()
            print("The result of your floor division is",str(result)+".")
        elif int(choice) == 10:
            result = exponentiation()
            print("The result of your exponentiation is",str(result)+".")
    print("Thank you for using Simple Calculator. Goodbye.")

result()