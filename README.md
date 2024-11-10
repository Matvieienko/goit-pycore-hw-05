# Assistant Bot


## Installation Instructions

To run the bot, please follow these steps:

1. Install Python (version 3.8 or newer):
   You can download it [here](https://www.python.org/downloads/).

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

| Command           | Arguments                    | Description                                                                                     |
|-------------------|------------------------------|-------------------------------------------------------------------------------------------------|
| `add-contact`     | `<name> <phone>`             | Add a new contact with a name and phone number, or add a phone number to an existing contact.   |
| `update-contact`  | `<name> <old phone> <new phone>` | Change the phone number for the specified contact.                                         |
| `set-birthday`    | `<name> <DD.MM.YYYY>`        | Set a birthday date for the specified contact.                                                  |
| `show-birthday`   | `<name>`                     | Show the birthday date for the specified contact.                                               |
| `upcoming-birthdays` | `<days>`                  | Show upcoming birthdays within the specified days.                                              |
| `set-email`       | `<name> <email>`             | Set the email for the specified contact.                                                        |
| `set-address`     | `<name> <address>`           | Set the address for the specified contact.                                                      |
| `get-contact`     | `<name>`                     | Show phone numbers for the specified contact.                                                   |
| `all-contacts`    |                              | Show all contacts in the address book.                                                          |
| `search-contact`  | `<value>`                    | Search for a contact by any value in their details.                                             |
| `delete-contact`  | `<name>`                     | Delete the specified contact.                                                                   |

### 🗒️ Note Management

| Command         | Arguments               | Description                                                                    |
|-----------------|-------------------------|--------------------------------------------------------------------------------|
| `add-note`      |                         | Add a new note.                                                                |
| `all-notes`     |                         | Show all notes in the notebook.                                                |
| `search-notes`  |                         | Search for a certain notes based on the title, tags, or content.               |
| `delete-notes`  |                         | Delete notes from the notebook.                                                |
| `edit-note`     |                         | Edit a note from the notebook.                                                 |

### ℹ️ General Commands

| Command   | Description                    |
|-----------|--------------------------------|
| `help`    | Show commands table.           |
| `exit`    | Save data and close the application. |


## Example Command to Run:

```bash
python main.py