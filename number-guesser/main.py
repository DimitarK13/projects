import random


def generate_random_number() -> int:
    return random.randrange(101) 


def compare_numbers(x: int, y: int) -> str:
    if x == y:
        return 'Congratulations!🥳'
    elif x < y:
        return 'Your number is too small'
    else:
        return 'Your number is too big'


def play_game():
    count = 0
    guess = -1
    random_number = generate_random_number()

    while guess != random_number:
        try:
            guess = int(input('Enter a number 0-100: '))

            if guess < 0 or guess > 100:
                print('Value must be between 0 and 100')
                continue

            count += 1

            result = compare_numbers(guess, random_number)

            print(result)

        except ValueError:
            print('Well that\'s not a number now is it?')
            
    print(f'Took you a total of {count} guesses')


if __name__ == '__main__':
    while True:
        play_game()

        if input('Fancy another game? (y/n) ') != 'y':
            print('Later gator')
            break