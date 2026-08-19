import random

def random_number_generator() -> int:
    return random.randrange(101) 


def compare_numbers(x: int, y: int) -> dict[bool, str]:
    if x == y:
        return {True: 'Congratulations!🥳 Took you a total of'}

    if x < y:
        return{False: 'Your number is too small'}

    if x > y:
        return{False: 'Your number is too big'}

    return {False: ''}


def main(random_number: int, count: int):
    count += 1

    try:
        user_input = int(input('Enter a number 0-100: '))

        if user_input < 0 or user_input > 100:
            print('Value must be between 0 and 100 ')

        result = compare_numbers(user_input, random_number)

        if next(iter(result)) == False:
            print(next(iter(result.values())))
            main(random_number, count)


        if next(iter(result)) == True:
            print(f'{next(iter(result.values()))} {count} guesses')

            if input('Fancy another game? (y/n) ') == 'y':
                main(random_number_generator(), 0)
            else:
                print('Later gator')

    except ValueError:
        print('Well that\'s not a number now is it?')
        main(random_number, count)

main(random_number_generator(), 0)