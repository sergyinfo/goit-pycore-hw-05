"""
This module contains the main function of the assistant bot.

The main function reads user input, parses it, and calls the appropriate command handler function.

The assistant bot can perform the following commands:
- hello: Display a greeting message.
- add: Add a contact to the contacts dictionary.
- change: Change the phone number of an existing contact.
- phone: Show the phone number of a contact.
- all: Show all contacts in the contacts dictionary.
- close or exit: Close the assistant bot.
"""
from .command_handlers import add_contact, change_contact, show_phone, show_all

def parse_input(user_input):
    """
    Parse the user input into a command and arguments.

    Args:
    user_input (str): The user input string.

    Returns:
    tuple: A tuple containing the command (str) and arguments (list).
    """
    parts = user_input.strip().split()
    command = parts[0].lower() if parts else None
    args = parts[1:]
    return command, args

def main():
    """
    The main function of the assistant bot.
    """
    contacts = {}
    print("Welcome to the assistant bot!")

    while True:
        user_input = input("Enter a command: ")
        command, args = parse_input(user_input)

        match command:
            case "close" | "exit":
                print("Good bye!")
                break
            case "hello":
                print("How can I help you?")
            case "add":
                print(add_contact(args, contacts))
            case "change":
                print(change_contact(args, contacts))
            case "phone":
                print(show_phone(args, contacts))
            case "all":
                print(show_all(contacts))
            case None:
                print("Please enter a command.")
            case _:
                print("Invalid command.")

if __name__ == "__main__":
    main()
