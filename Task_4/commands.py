from colorama import Fore
from decorators import input_error

@input_error
def add_contact(args, contacts):
    if len(args) != 2:
        return Fore.RED + "Invalid input. Use format: add [name] [phone]"
    
    name, phone = args
    contacts[name] = phone
    return Fore.GREEN + f"Contact '{name}' added."

@input_error
def change_contact(args, contacts):
    if len(args) != 2:
        return Fore.RED + "Invalid input. Use format: change [name] [new_phone]"
    
    name, new_phone = args
    if name in contacts:
        contacts[name] = new_phone
        return Fore.GREEN + f"Contact '{name}' updated."
    else:
        return Fore.RED + f"Contact '{name}' not found."

@input_error
def show_phone(args, contacts):
    if len(args) != 1:
        return Fore.RED + "Invalid input. Use format: phone [name]"
    
    name = args[0]
    if name in contacts:
        return Fore.GREEN + f"👨 {name} ☎️  {contacts[name]}"
    else:
        return Fore.RED + f"Contact '{name}' not found."

@input_error
def show_all(contacts):
    if contacts:
        return Fore.GREEN + "\n".join([f"👨 {name} ☎️  {phone}" for name, phone in contacts.items()])
    else:
        return Fore.RED + "No contacts available."