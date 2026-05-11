def calculator(a, b):
    calc = input("Enter the operation: ")
    question = input("Y/N: ")
    while question == "Y":
        match calc:
            case "+":
                print(f"The sum of {a} and {b} is {a+b}")
            case "-":
                print(f"The sum of {a} and {b} is {a+b}")
            case "/":
                print(f"The sum of {a} and {b} is {a+b}")

            case "+":
                print(f"The sum of {a} and {b} is {a+b}")

calculator()
