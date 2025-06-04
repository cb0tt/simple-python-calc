def add(number_one, number_two):
    return number_one + number_two

def subtract(number_one, number_two):
    return number_one - number_two

def multiply(number_one, number_two):
    return number_one * number_two

def divide(number_one, number_two):
    return number_one / number_two

operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
}


def calc():
    still_going = True
    num_one = float(input("What is the first number:"))

    while still_going:
        operator_type = input("Pick and operator, ('+' '-' '*' '/':")
        if operator_type not in ['+', '-', '*', '/']:
            print("Not a valid operation.")
        num_two = float(input("What is the next number:"))
        calculation_function = operations[operator_type]
        answer = operations[operator_type](num_one, num_two)
        print(f"{num_one}{operator_type}{num_two} = {answer}")

        go_again = input(f"Type 'y' to continue with {answer} or type 'n' to choose a new number. ").lower()
        if go_again == "y":
            num_one = answer
        else:
            break
calc()










