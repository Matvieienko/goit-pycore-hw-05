# Assistant Bot


## Installation Instructions

To run the bot, please follow these steps:

1. Install Python. You can download it [here](https://www.python.org/downloads/).

2. Run the following command to install all necessary packages:

    ```bash
    pip install -r requirements.txt
    ```

3. Start the bot using the following command:

    ```bash
    python main.py
    ```

## List of Commands

### 📇 Contact Management

| Command              | Description                                                                                     |
|----------------------|-------------------------------------------------------------------------------------------------|
| `add-contact`        | Add a new contact with a name and phone number, or add a phone number to an existing contact.   |
| `update-contact`     | Change the phone number for the specified contact.                                              |
| `set-birthday`       | Set a birthday date for the specified contact.                                                  |
| `show-birthday`      | Show the birthday date for the specified contact.                                               |
| `upcoming-birthdays` | Show upcoming birthdays within the specified days.                                              |
| `set-email`          | Set the email for the specified contact.                                                        |
| `set-address`        | Set the address for the specified contact.                                                      |
| `get-contact`        | Show phone numbers for the specified contact.                                                   |
| `all-contacts`       | Show all contacts in the address book.                                                          |
| `search-contact`     | Search for a contact by any value in their details.                                             |
| `delete-contact`     | Delete the specified contact.                                                                   |

### 🗒️ Note Management

| Command         | Description                                                                    |
|-----------------|--------------------------------------------------------------------------------|
| `add-note`      | Add a new note.                                                                |
| `all-notes`     | Show all notes in the notebook.                                                |
| `search-notes`  | Search for a certain notes based on the title, tags, or content.               |
| `delete-notes`  | Delete notes from the notebook.                                                |
| `edit-note`     | Edit a note from the notebook.                                                 |

### ℹ️ General Commands

| Command   | Description                    |
|-----------|--------------------------------|
| `help`    | Show commands table.           |
| `exit`    | Save data and close the application. |


## Example
```
👀 Enter a command:  add-contact
👉 Enter name:  John
👉 Enter phone:  1234567890
Phone {1234567890} already exists for record {John}.


👀 Enter a command:  set-birthday
👉 Enter name:  John
👉 Enter birthday in a DD.MM.YYYY date format:  01.01.1990
Contact updated!


👀 Enter a command:  all-contacts
1990-01-01
🦐JOHN
[1234567890]
... | ...


The end!


👀 Enter a command:  exit
Good bye!```