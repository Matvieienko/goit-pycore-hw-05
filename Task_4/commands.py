from colorama import Fore
from decorators import input_error

@input_error
def add_contact(args, contacts):
    name, phone = args
    contacts[name] = phone
    return Fore.GREEN + f"✅ Contact '{name}' added."

@input_error
def change_contact(args, contacts):
    name, new_phone = args
    if name in contacts:
        contacts[name] = new_phone
        return Fore.GREEN + f"🔄 Contact '{name}' updated."
    else:
        raise KeyError

@input_error
def show_phone(args, contacts):
    name = args[0]
    if name in contacts:
        return Fore.GREEN + f"👨 {name}  ☎️   {contacts[name]}"
    else:
        raise KeyError

# Декоратор тут не потрібний, так як функція не приймає аргументів 
def show_all(contacts):
    if contacts:
        return Fore.GREEN + "\n".join([f"👨 {name}  ☎️   {phone}" for name, phone in contacts.items()])
    else:
        return Fore.RED + "🔍 No contacts available."