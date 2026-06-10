# ******* MY FIRST PROJECT CALCULATOR*******

print("Welcome to Calculator")

while True:

    print("\nChoose an operation")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Modulo")
    print("6. Quit")

    choice = input("Enter your choice : ")

    # Quit option
    if choice == "6":
        print("Goodbye!")
        break

    # Taking numbers from user
    num1 = float(input("Enter first number : "))
    num2 = float(input("Enter second number : "))
 
    # Addition
    if choice == "1":
        result = num1 + num2
        print("You chossed the Addition so, the Answer =", result)

    # Subtraction
    elif choice == "2":
        result = num1 - num2
        print("You chossed the Subtraction so, the Answer =", result)

    # Multiplication
    elif choice == "3":
        result = num1 * num2
        print("You chossed the Multiplication so, the Answer =", result)

    # Division
    elif choice == "4":

        if num2 == 0:
            print("Cannot divide by zero")

        else:
            result = num1 / num2
            print("You chossed the Division so, the Answer =", result)

    # Modulo
    elif choice == "5":

        if num2 == 0:
            print("Cannot modulo by zero")

        else:
            result = num1 % num2
            print("You chossed the Modulo so, the Answer =", result)

    # Invalid choice
    else:
        print("Invalid choice")