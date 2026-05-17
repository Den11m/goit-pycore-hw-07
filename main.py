from address_book import AddressBook
from handlers import (
    add_birthday,
    add_contact,
    change_contact,
    show_all,
    show_birthday,
    show_phone,
    upcoming_birthdays,
)


COMMANDS = {
    "add": add_contact,
    "change": change_contact,
    "phone": show_phone,
    "all": show_all,
    "add-birthday": add_birthday,
    "show-birthday": show_birthday,
    "birthdays": upcoming_birthdays,
}

EXIT_COMMANDS = {"close", "exit"}


def parse_input(user_input: str) -> tuple[str, list[str]]:
    parts = user_input.strip().split()
    if not parts:
        return "", []
    cmd, *args = parts
    return cmd.lower(), args


def main() -> None:
    book = AddressBook()
    print("Welcome to the assistant bot!")
    while True:
        try:
            user_input = input("Enter a command: ")
        except (EOFError, KeyboardInterrupt):
            print("\nGood bye!")
            break

        command, args = parse_input(user_input)

        if not command:
            continue
        if command in EXIT_COMMANDS:
            print("Good bye!")
            break
        if command == "hello":
            print("How can I help you?")
            continue

        handler = COMMANDS.get(command)
        if handler is None:
            print("Invalid command.")
            continue

        print(handler(args, book))


if __name__ == "__main__":
    main()
