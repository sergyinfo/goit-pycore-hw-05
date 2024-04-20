"""
This module contains functions 
that handle the different commands that the assistant bot can receive.
"""

from .decorators import input_error

@input_error
def add_contact(args, contacts):
    """
    Add a contact to the contacts dictionary.

    Args:
    args (list): A list containing the name and phone number of the contact.
    contacts (dict): A dictionary containing the contacts.

    Returns:
    str: A message indicating whether the contact was added successfully or not.

    Raises:
    ValueError: If the number of arguments is not equal to 2.
    """
    if len(args) != 2:
        raise ValueError("Add command requires a name and a phone number.")
    name, phone = args
    contacts[name] = phone
    return "Contact added."

@input_error
def change_contact(args, contacts):
    """
    Change the phone number of an existing contact.

    Args:
    args (list): A list containing the name and new phone number of the contact.
    contacts (dict): A dictionary containing the contacts.

    Returns:
    str: A message indicating whether the contact was updated successfully or not.

    Raises:
    ValueError: If the number of arguments is not equal to 2 or if the contact is not found.
    """
    if len(args) != 2:
        raise ValueError("Change command requires a name and a new phone number.")
    name, new_phone = args
    if name in contacts:
        contacts[name] = new_phone
        return "Contact updated."
    raise ValueError("Contact not found")

@input_error
def show_phone(args, contacts):
    """
    Show the phone number of a contact.

    Args:
    args (list): A list containing the name of the contact.
    contacts (dict): A dictionary containing the contacts.

    Returns:
    str: The phone number of the contact or an error message if the contact is not found.

    Raises:
    ValueError: If the number of arguments is not equal to 1 or if the contact is not found.
    """
    if len(args) != 1:
        raise ValueError("Phone command requires a name.")
    name = args[0]
    if name in contacts:
        return f"{name}: {contacts[name]}"
    raise ValueError("Contact not found")

@input_error
def show_all(contacts):
    """
    Show all contacts in the contacts dictionary.

    Args:
    contacts (dict): A dictionary containing the contacts.

    Returns:
    str: A formatted string containing all the contacts or a message if no contacts are found.

    Raises:
    ValueError: If the contacts dictionary is empty.
    """
    if not contacts:
        raise ValueError("No contacts were found")
    return "\n".join(f"{name}: {phone}" for name, phone in contacts.items())
