from Art import logo


def add(n1,n2):
    return int(n1 + n2)

def multiple(n1,n2):
    return int(n1 * n2)

def substract(n1,n2):
    return int(n1 - n2)

def divide(n1,n2):
    return int(n1 / n2)

operations = {
    "+": add,
    "*": multiple,
    "-": substract,
    "/": divide
}
def calculator():
    print(logo)
    num1 = float(input("What is your first number? "))

    for operate in operations:
        print(operate)
    should_continue = True

    while should_continue:
        operation_symbol = input("Pick an operation: ")
        num2 = float(input("Pick the next number "))
        if operation_symbol in operations:
            calculation_function = operations[operation_symbol]
            result = calculation_function(num1, num2)
            print(f"{num1} {operation_symbol} {num2} = {result}")
        ctn = input( f"Type 'yes' to continue calculating with {result}, type 'n' to a new calculation or type 'exit' to finish the process ").lower()

        if ctn == 'yes':
            calculator()
        elif ctn == "exit":
            return "Process finished"
        else:
            should_continue = False
            calculator()

calculator()





















