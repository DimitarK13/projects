def add(x: float, y: float) -> float:
    return x + y


def subtract(x: float, y: float) -> float:
    return x - y


def multiply(x: float, y: float) -> float:
    return x * y


def divide(x: float, y: float) -> float:
    return x / y


def calculate() -> bool:
    try:
        x = float(input('Enter first number '))
        y = float(input('Enter second number '))
        calculation = input('Choose your operation (+ - * / q) ')

        match calculation:
            case '+':
                print(add(x, y))
            case '-':
                print(subtract(x, y))
            case '*':
                print(multiply(x, y))
            case '/':
                print(divide(x, y))
            case 'q':
                return True
            case _:
                print('Invalid operation')

    except ValueError:
        print('Not a number')

    except ZeroDivisionError:
        print('Division by zero is not possible')

    return False


while True:
    have_quit = calculate()

    if have_quit:
        break