def calculator():
    print("Welcome to the Basic Calculator!")
    
    while True:
        # Input for numbers
        try:
            num1 = float(input("\nEnter the first number (or type 'exit' to quit): "))
        except ValueError:
            print("Invalid input! Please enter numeric values or type 'exit' to quit.")
            continue

        try:
            num2 = float(input("Enter the second number: "))
        except ValueError:
            print("Invalid input! Please enter numeric values.")
            continue

        # Display available operations
        print("\nChoose an operation:")
        print("1. Addition (+)")
        print("2. Subtraction (-)")
        print("3. Multiplication (*)")
        print("4. Division (/)")
        print("Type 'exit' to quit the calculator.")

        # Input for operation
        operation = input("Enter the number corresponding to the operation (1/2/3/4): ").strip()

        # Check for exit condition
        if operation.lower() == "exit":
            print("\nExiting the calculator. Goodbye!")
            break

        # Perform the selected operation
        if operation == '1':
            result = num1 + num2
            print(f"\nThe result of addition is: {result}")
        elif operation == '2':
            result = num1 - num2
            print(f"\nThe result of subtraction is: {result}")
        elif operation == '3':
            result = num1 * num2
            print(f"\nThe result of multiplication is: {result}")
        elif operation == '4':
            if num2 == 0:
                print("\nDivision by zero is not allowed.")
            else:
                result = num1 / num2
                print(f"\nThe result of division is: {result}")
        else:
            print("\nInvalid operation selected. Please choose 1, 2, 3, or 4.")
        
        # Loop continues until the user explicitly types "exit"

# Run the calculator
calculator()
