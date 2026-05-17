from functools import wraps

from address_book import AddressBook, Record


def input_error(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ValueError as e:
            msg = str(e)
            if "not enough values to unpack" in msg or "too many values to unpack" in msg:
                return "Invalid number of arguments."
            return msg or "Invalid value."
        except KeyError:
            return "Contact not found."
        except IndexError:
            return "Invalid number of arguments."
    return wrapper


def _get_record(book: AddressBook, name: str) -> Record:
    record = book.find(name)
    if record is None:
        raise KeyError(name)
    return record


@input_error
def add_contact(args: list[str], book: AddressBook) -> str:
    name, phone, *_ = args
    record = book.find(name)
    if record is None:
        record = Record(name)
        book.add_record(record)
        message = "Contact added."
    else:
        message = "Contact updated."
    if phone:
        record.add_phone(phone)
    return message


@input_error
def change_contact(args: list[str], book: AddressBook) -> str:
    name, old_phone, new_phone, *_ = args
    record = _get_record(book, name)
    if not record.edit_phone(old_phone, new_phone):
        return "Phone not found."
    return "Phone updated."


@input_error
def show_phone(args: list[str], book: AddressBook) -> str:
    (name,) = args[:1] or [None]
    if name is None:
        raise IndexError
    record = _get_record(book, name)
    if not record.phones:
        return "No phones for this contact."
    return "; ".join(str(p) for p in record.phones)


@input_error
def show_all(_args: list[str], book: AddressBook) -> str:
    return str(book)


@input_error
def add_birthday(args: list[str], book: AddressBook) -> str:
    name, birthday, *_ = args
    record = _get_record(book, name)
    record.add_birthday(birthday)
    return "Birthday added."


@input_error
def show_birthday(args: list[str], book: AddressBook) -> str:
    (name,) = args[:1] or [None]
    if name is None:
        raise IndexError
    record = _get_record(book, name)
    if record.birthday is None:
        return "Birthday not set for this contact."
    return str(record.birthday)


@input_error
def upcoming_birthdays(_args: list[str], book: AddressBook) -> str:
    upcoming = book.get_upcoming_birthdays()
    if not upcoming:
        return "No upcoming birthdays in the next week."
    lines = ["Upcoming birthdays:"]
    lines += [f"{item['name']}: {item['congratulation_date']}" for item in upcoming]
    return "\n".join(lines)
