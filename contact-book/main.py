from dataclasses import dataclass
import json
from pathlib import Path


@dataclass
class ContactDetails:
    name: str
    number: str
    email: str


class Contact:
    def __init__(self, info: ContactDetails) -> None:
        self.name = info.name
        self.number = info.number
        self.email = info.email


    def update_contact(self, info: ContactDetails) -> None:
        if info.name:
            self.name = info.name

        if info.number:
            self.number = info.number

        if info.email:
            self.email = info.email


def get_contacts(contacts: list[Contact]) -> None:
    """Get a list of all contacts"""

    if not contacts:
        print('No contacts yet')
        return

    for i, contact in enumerate(contacts):
        print(f"{i}: {contact.name} ({contact.email}) - {contact.number}")


def add_contact(info: ContactDetails, contacts: list[Contact]) -> None:
    """Add a new contact to a list (passed as an argument)"""

    contacts.append(Contact(info))
    save_contacts(contacts)


def get_single_contact(name: str, contacts: list[Contact]) -> None:
    """Get a single contact searched by name from a list (passed as an argument)"""

    contact = next((contact for contact in contacts if contact.name.lower() == name.lower()), None)

    if contact:
        print(f"{contact.name} ({contact.email}) - {contact.number}")
    else:
        print('No contact with that name found')


def update_contact(contact_id: int, info: ContactDetails, contacts: list[Contact]) -> None:
    """Update contact based on id in a list (passed as an argument)"""

    try:
        contacts[contact_id].update_contact(info)
        save_contacts(contacts)
        print('Successfully updated contact')
    except IndexError:
        print(f'Contact with index {contact_id} doesn\'t exist')


def delete_contact(contact_id: int, contacts: list[Contact]) -> None:
    """Delete a contact based on id in a list (passed as an argument)"""

    try:
        del contacts[contact_id]
        save_contacts(contacts)
        print('Successfully deleted contact')
    except IndexError:
        print(f'Contact with index {contact_id} doesn\'t exist')


file_name = Path('contacts.json')
contacts: list[Contact] = []


if file_name.exists():
    try:
        with open(file_name, 'r', encoding='utf-8') as file:
            raw_data = json.load(file)

            contacts = [Contact(ContactDetails(item['name'], item['number'], item['email'])) for item in raw_data]

    except KeyError:
        contacts = []
        print('Invalid JSON data')
        
    except json.JSONDecodeError:
        contacts = []
        print('JSON cannot be decoded')


def save_contacts(contacts: list[Contact]) -> None:
    """Save contacts to a local json file"""

    with open(file_name, 'w', encoding='utf-8') as file:
        json.dump(contacts, file, default=lambda o: o.__dict__, indent=4)



def get_contact_input() -> ContactDetails | None:
    name = input('Enter contact name: ')
    number = input('Enter contact number: ')
    email = input('Enter contact email: ')

    if name and number and email:
        return ContactDetails(name, number, email)
    else:
        print('Missing one or more required fields')


def handle_actions(contacts: list[Contact]) -> bool:
    try:
        user_action = input('Choose action (g a s u d q): ')

        match user_action.lower():
            case 'g':
                get_contacts(contacts)

            case 'a':
                contact_info = get_contact_input()

                if contact_info:
                    add_contact(contact_info, contacts)

            case 's':
                search_input = input('Enter name to search by: ')

                get_single_contact(search_input, contacts)

            case 'u':
                contact_id = int(input('Enter contact ID: '))
                contact_info = get_contact_input()
                
                if contact_info:
                    update_contact(contact_id, contact_info, contacts)

            case 'd':
                contact_id = int(input('Enter contact ID: '))

                delete_contact(contact_id, contacts)

            case 'q':
                return True

            case _:
                print('Invalid action key')

    except ValueError:
        print('Not a valid number')

    return False


if __name__ == '__main__':
    while True:
        has_quit = handle_actions(contacts)

        if has_quit:
            break