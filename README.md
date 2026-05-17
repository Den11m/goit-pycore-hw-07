# Address Book Bot


```bash
python3 main.py
```

## Features

- Add, update, and remove phone numbers
- Store and display birthdays
- Get upcoming birthdays for the next week
- Weekend-aware birthday congratulation dates
- Input validation (10-digit phones, DD.MM.YYYY dates)

## Commands

| Command | Description | Example |
|---------|-------------|---------|
| `hello` | Greeting | `hello` |
| `add [name] [phone]` | Add contact or update phone | `add John 1234567890` |
| `change [name] [old_phone] [new_phone]` | Change phone number | `change John 1234567890 0987654321` |
| `phone [name]` | Show contact's phones | `phone John` |
| `all` | Show all contacts | `all` |
| `add-birthday [name] [date]` | Add birthday (DD.MM.YYYY) | `add-birthday John 20.05.1990` |
| `show-birthday [name]` | Show contact's birthday | `show-birthday John` |
| `birthdays` | Show upcoming birthdays (next 7 days) | `birthdays` |
| `close` / `exit` | Exit the program | `close` |

## Validation

- **Phone numbers**: Must contain exactly 10 digits
- **Birthdays**: Must be in DD.MM.YYYY format
- **Contact names**: Cannot be empty

## Example Session

```
Welcome to the assistant bot!
Enter a command: hello
How can I help you?
Enter a command: add John 1234567890
Contact added.
Enter a command: add Alice 9876543210
Contact added.
Enter a command: add-birthday John 20.05.1990
Birthday added.
Enter a command: add-birthday Alice 15.05.1990
Birthday added.
Enter a command: all
Contact name: John, phones: 1234567890, birthday: 20.05.1990
Contact name: Alice, phones: 9876543210, birthday: 15.05.1990
Enter a command: birthdays
Upcoming birthdays:
Alice: 19.05.2026
John: 20.05.2026
Enter a command: change John 1234567890 5555555555
Phone updated.
Enter a command: phone John
5555555555
Enter a command: exit
Good bye!
```

## Error Handling

The bot provides clear error messages for:
- Invalid command format
- Missing or incorrect arguments
- Contact not found
- Invalid phone number format
- Invalid date format
