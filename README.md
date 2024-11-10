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
| `upcoming-birthdays` | `<days>`                  | Show upcoming birthdays within the specified number of days.                                    |
| `set-email`       | `<name> <email>`             | Set the email for the specified contact.                                                        |
| `set-address`     | `<name> <address>`           | Set the address for the specified contact.                                                      |
| `get-contact`     | `<name>`                     | Show phone numbers for the specified contact.                                                   |
| `all-contacts`    | None                         | Display all contacts in the address book.                                                       |
| `search-contact`  | `<value>`                    | Search for a contact by any value in their details.                                             |
| `delete-contact`  | `<name>`                     | Delete the specified contact.                                                                   |

### 🗒️ Note Management

| Command         | Arguments               | Description                                                                    |
|-----------------|-------------------------|--------------------------------------------------------------------------------|
| `add-note`      |                         | Add a new note.                                                                |
| `all-notes`     |                         | Display all notes in the notebook.                                             |
| `search-notes`  |                         | Search for notes based on the title, tags, or content.                         |
| `delete-notes`  |                         | Delete notes from the notebook.                                                |
| `edit-note`     |                         | Edit a note in the notebook.                                                   |

### ℹ️ General Commands

| Command   | Description                    |
|-----------|--------------------------------|
| `help`    | Show the commands table.       |
| `exit`    | Save data and close the application. |

## Project Structure

- **main.py** – The main file to run the bot.
- **console_bot.py** – Contains the main logic of the bot.
- **address_book_models.py** – Modules for contact management.
- **notes_models.py** – Modules for note management.
- **exceptions.py** – File for handling exceptions.
- **cli_interface.py** – Command line interface for interacting with the bot.

## Libraries Used

- **questionary** – For the interactive command line interface.
- **prettytable** – For displaying commands in table format.
- **logging** – For logging events.

## Example Command to Run:

```bash
python main.py