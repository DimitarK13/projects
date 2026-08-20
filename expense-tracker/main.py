# Coffee $2 (Necessity)
# Spotify $10 (Subscriptions)
# Netflix $12 (Subscriptions)
# Keyboard $100 (Work)
from collections import defaultdict


class Expense:
    def __init__(self, description: str, amount: float, category: str) -> None:
        self.amount = amount
        self.description = description
        self.category = category


    def update_category(self, category: str) -> None:
        self.category = category


expenses: list[Expense] = []


def get_total_spending(expenses_list: list[Expense]) -> None:
    print(f"Total spending: ${sum(expense.amount for expense in expenses_list)}")


def get_spending_by_category(expenses_list: list[Expense]) -> None:
    if not expenses_list:
        print('No expenses yet. Add your first expense by pressing \'a\'')
        return

    amounts: dict[str, float] = defaultdict(float)

    for expense in expenses_list:
        amounts[expense.category] += expense.amount

    for key, value in amounts.items():
        print(f'{key}: ${value}')



def get_all_expenses(expenses_list: list[Expense]) -> None:
    if not expenses_list:
        print('No expenses yet. Add your first expense by pressing \'a\'')
        return
    
    for i, expense in enumerate(expenses_list):
        print(f"{i}: {expense.description} ${expense.amount} ({expense.category})")


def add_new_expense(description: str, amount: float, category: str, expenses_list: list[Expense]) -> None:
    expense = Expense(description, amount, category)
    expenses_list.append(expense)


def update_category(expense_id: int, category: str, expenses_list: list[Expense]) -> bool:
    try:
        expenses_list[expense_id].update_category(category)
        return True
    except IndexError:
        print(f'Item with index {expense_id} doesn\'t exist')
        return False



def handle_actions() -> bool:
    try:
        action_key = input('Choose action (a u p t c q): ')

        match action_key:
            case 'a' | 'A':
                description = input('Enter description: ')
                category = input('Enter category: ')
                amount = float(input('Enter amount ($): '))

                if amount <= 0 or not description or not category:
                    raise ValueError
                
                
                add_new_expense(description, amount, category, expenses)
                print('Item added successfully')

            case 'u' | 'U':
                item_id = int(input('Enter item ID: '))
                category = input('Enter new category: ')

                if not category:
                    raise ValueError

                result = update_category(item_id, category, expenses)

                if result:
                    print('Category updated successfully')

            case 'p' | 'P':
                get_all_expenses(expenses)

            case 't' | 'T':
                get_total_spending(expenses)

            case 'c' | 'C':
                get_spending_by_category(expenses)

            case 'q' | 'Q':
                return True

            case _:
                print('Invalid action key')
    except ValueError:
        print(f'Not a valid input')

    return False


if __name__ == '__main__':
    while True:
        has_quit = handle_actions()

        if has_quit:
            break