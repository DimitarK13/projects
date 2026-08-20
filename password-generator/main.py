from dataclasses import dataclass
import secrets
import string

@dataclass
class PasswordOptions:
    length: int
    has_upper_case: bool
    has_lower_case: bool
    has_numbers: bool
    has_special_chars: bool


def validate_input(password_options: PasswordOptions) -> bool:
    if password_options.length < 6:
        print('Password length must be 6 or more characters')
        return False

    if not password_options.has_lower_case and not password_options.has_upper_case:
        print('Password must have either upper case or lower case characters')
        return False

    return True


def generate_password(password_options: PasswordOptions) -> str:
    alphabet = ''

    if password_options.has_upper_case:
        alphabet = string.ascii_uppercase

    if password_options.has_lower_case:
        alphabet += string.ascii_lowercase

    if password_options.has_numbers:
        alphabet += string.digits

    if password_options.has_special_chars:
        alphabet += string.punctuation

    password = "".join(secrets.choice(alphabet) for _ in range(password_options.length))

    return password


def handle_actions() -> None:
    try:
        pass_length = int(input('Enter password length (minimum 6 characters): '))
        has_upper_case = input('Should password have upper case letters? (y/n): ').lower() == 'y'
        has_lower_case = input('Should password have lower case letters? (y/n): ').lower() == 'y'
        has_numbers = input('Should password have numbers? (y/n): ').lower() == 'y'
        has_special_characters = input('Should password have special characters? (y/n): ').lower() == 'y'

        options = PasswordOptions(pass_length, has_upper_case, has_lower_case, has_numbers, has_special_characters)

        is_valid = validate_input(options)

        if is_valid:
            password = generate_password(options)
            print(password)
            
    except ValueError:
        print('Password length must be a number')

handle_actions()