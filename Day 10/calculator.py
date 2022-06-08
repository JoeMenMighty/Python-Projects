from art import logo
from click import clear

print(logo)

def add(num1, num2):
    return num1 + num2

def subtract(num1, num2):
    return num1 - num2

def multiply(num1, num2):
    return num1 * num2

def divide(num1, num2):
    return num1 / num2

operators = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
}

# first_num = int(input("Enter the first number: "))
# restart = True
# continue_status = True
      
# while restart:
#     if continue_status:
#         first_num = int(input("Enter the first number: "))
#     for symbol in operators:
#         print(symbol)   
#     operation_symbol = input("Please choose your operator from above.")
#     second_num = int(input("Enter the next number: "))

#     calculation_func = operators[operation_symbol]
#     answer = calculation_func(first_num, second_num)

#     print(f"{first_num} {operation_symbol} {second_num} = {answer}")

#     cont = input(f"Do you want to continue calculating with {answer}? type 'y' to continue or 'n' to exit: ")
#     if cont == "n":
#         clear()
#         continue_status = True
#     elif cont == "y":
#         first_num = answer
#         continue_status = False
        

# or using recursive functions
def calculator():
    first_num = float(input("Enter the first number: "))
    restart = True
    while restart:
        for symbol in operators:
            print(symbol)   
        operation_symbol = input("Please choose your operator from above.")
        second_num = float(input("Enter the next number: "))

        calculation_func = operators[operation_symbol]
        answer = calculation_func(first_num, second_num)

        print(f"{first_num} {operation_symbol} {second_num} = {answer}")

        cont = input(f"Do you want to continue calculating with {answer}? type 'y' to continue or 'n' to exit: ")
        if cont == "n":
            clear()
            calculator()
        elif cont == "y":
            first_num = answer
            continue_status = False


calculator()
