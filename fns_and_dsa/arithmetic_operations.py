def perform_operation():
    num1 = float(input("Enter the first number:"))
    num2 = float(input("Enter the second number:"))
    operation =input("Enter the operation (add, subtract, multiply, divide): ").strip().lower()
    match operation:
        case "add":
            result = num1 + num2
            print(f"The result is {result}.")
        case "subtract":
            result = num1 - num2
            print(f"The result is {result}.")
        case "multiply":
            result = num1 * num2
            print(f"The result is {result}.")
        case "divide":
            if num2 == 0:
                print("cannot divide by 0")
            else:
                result = num1 / num2
                print(f"The result is {result}.")
perform_operation()