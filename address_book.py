from collections import UserDict
from datetime import datetime, date, timedelta
from typing import Optional


class Field:
    def __init__(self, value):
        self.value = value

    def __str__(self) -> str:
        return str(self.value)


class Name(Field):
    def __init__(self, value: str):
        if not value or not value.strip():
            raise ValueError("Name cannot be empty.")
        super().__init__(value.strip())


class Phone(Field):
    LENGTH = 10

    def __init__(self, value: str):
        if not (value.isdigit() and len(value) == self.LENGTH):
            raise ValueError(f"Phone number must contain {self.LENGTH} digits.")
        super().__init__(value)


class Birthday(Field):
    FORMAT = "%d.%m.%Y"

    def __init__(self, value: str):
        try:
            parsed = datetime.strptime(value, self.FORMAT).date()
        except ValueError:
            raise ValueError("Invalid date format. Use DD.MM.YYYY")
        super().__init__(parsed)

    def __str__(self) -> str:
        return self.value.strftime(self.FORMAT)


class Record:
    def __init__(self, name: str):
        self.name = Name(name)
        self.phones: list[Phone] = []
        self.birthday: Optional[Birthday] = None

    def add_phone(self, phone: str) -> None:
        if self.find_phone(phone):
            return
        self.phones.append(Phone(phone))

    def remove_phone(self, phone: str) -> bool:
        existing = self.find_phone(phone)
        if existing is None:
            return False
        self.phones.remove(existing)
        return True

    def edit_phone(self, old_phone: str, new_phone: str) -> bool:
        for i, p in enumerate(self.phones):
            if p.value == old_phone:
                self.phones[i] = Phone(new_phone)
                return True
        return False

    def find_phone(self, phone: str) -> Optional[Phone]:
        return next((p for p in self.phones if p.value == phone), None)

    def add_birthday(self, birthday: str) -> None:
        self.birthday = Birthday(birthday)

    def __str__(self) -> str:
        phones = "; ".join(str(p) for p in self.phones) or "—"
        birthday = f", birthday: {self.birthday}" if self.birthday else ""
        return f"Contact name: {self.name}, phones: {phones}{birthday}"


class AddressBook(UserDict):
    def add_record(self, record: Record) -> None:
        self.data[record.name.value] = record

    def find(self, name: str) -> Optional[Record]:
        return self.data.get(name)

    def delete(self, name: str) -> bool:
        return self.data.pop(name, None) is not None

    def get_upcoming_birthdays(self, days: int = 7) -> list[dict]:
        today = datetime.now().date()
        result: list[dict] = []

        for record in self.data.values():
            if record.birthday is None:
                continue
            congrats_date = self._next_congratulation_date(record.birthday.value, today)
            if 0 <= (congrats_date - today).days <= days:
                result.append({
                    "name": record.name.value,
                    "congratulation_date": congrats_date.strftime(Birthday.FORMAT),
                })
        return result

    @staticmethod
    def _next_congratulation_date(birthday: date, today: date) -> date:
        next_birthday = birthday.replace(year=today.year)
        if next_birthday < today:
            next_birthday = birthday.replace(year=today.year + 1)
        if next_birthday.weekday() >= 5:
            next_birthday += timedelta(days=7 - next_birthday.weekday())
        return next_birthday

    def __str__(self) -> str:
        if not self.data:
            return "Address book is empty."
        return "\n".join(str(record) for record in self.data.values())
