import random

def random_number_generator() -> int:
    return random.randrange(100) 


def compare_numbers(x: int, y: int) -> bool:
    if x == y:
        return True

    if x < y:
        print('Your number is too small')

    if x > y:
        print('Your number is too big')

    return False


def main(random_number: int, count: int):
    count += 1

    try:
        user_input = int(input('Enter a number 0-100: '))

        if user_input < 0 or user_input > 100:
            print('Value must be between 0 and 100 ')

        res = compare_numbers(user_input, random_number)

        if res == False:
            main(random_number, count)


        if res == True:
            print(f'Congratulations!🥳 Took you a total of {count}')
            
            if input('Fancy another game? (y/n) ') == 'y':
                main(random_number_generator(), 0)
            else:
                print('Later gator')

    except ValueError:
        print('Well that\'s not a number now is it?')
        main(random_number_generator(), 0)

main(random_number_generator(), 0)