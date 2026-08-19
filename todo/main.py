class ListItem:
    def __init__(self, task: str, is_complete: bool = False) -> None:
        self.task = task
        self.is_complete = is_complete

    def update_status(self) -> None:
        self.is_complete = not self.is_complete


todo_list: list[ListItem] = []


def add_item(task: str) -> None:
    item = ListItem(task)

    todo_list.append(item)


def remove_item(item_id: int) -> None:
    try:
        del todo_list[item_id]
    except IndexError:
        print(f'Item with index {item_id} doesn\'t exist')


def update_item(item_id: int) -> None:
    try:
        todo_list[item_id].update_status()
    except IndexError:
        print(f'Item with index {item_id} doesn\'t exist')


def print_list() -> None:
    for i, item in enumerate(todo_list):
        print(f"{i}: {item.task} - {'Complete' if item.is_complete else 'In Progress'}")


def handle_actions() -> bool:
    key = input('Choose action (a d u q): ')

    try:
        match key:
            case 'a' | 'A':
                task_text = input('Enter todo item: ')
                add_item(task_text)
            case 'd' | 'D':
                task_id = int(input('Enter todo item id: '))
                remove_item(task_id)
            case 'u' | 'U':
                task_id = int(input('Enter todo item id: '))
                update_item(task_id)
            case 'q' | 'Q':
                return True
            case _:
                print('Not a valid action key')
    except ValueError:
        print('Enter a valid id value')

    print_list()
    return False


if __name__ == '__main__':
    while True:
        has_quit = handle_actions()

        if has_quit:
            break