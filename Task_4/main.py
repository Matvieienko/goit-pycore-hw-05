from colorama import Fore, init
from commands import add_contact, change_contact, show_phone, show_all
from decorators import input_error

init(autoreset=True)

def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, args

def main():
    contacts = {}
    print(Fore.BLUE + "Welcome to the assistant bot!")

    while True:
        user_input = input(Fore.BLUE + "Enter a command: ").strip()
        command, args = parse_input(user_input)

        if command in ["close", "exit"]:
            print(Fore.BLUE + "Good bye!")
            break
        elif command == "hello":
            print(Fore.BLUE + "How can I help you?")
        elif command == "add":
            print(add_contact(args, contacts))
        elif command == "change":
            print(change_contact(args, contacts))
        elif command == "phone":
            print(show_phone(args, contacts))
        elif command == "all":
            print(show_all(contacts))
        else:
            print(Fore.RED + "Invalid command.")

if __name__ == "__main__":
    main()