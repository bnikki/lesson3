num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
math_action = input("Enter math action: + - * / ")

match math_action:
    case "+":
        print(f"{num1} {math_action} {num2} = {num1 + num2}")
    case "-":
        print(f"{num1} {math_action} {num2} = {num1 - num2}")
    case "*":
        print(f"{num1} {math_action} {num2} = {num1 * num2}")
    case "/":
        if num2 != 0:
            print(f"{num1} {math_action} {num2} = {num1 / num2}")
        else:
            print("Division by zero!")
    case _:
        print("Incorrect math action!")
