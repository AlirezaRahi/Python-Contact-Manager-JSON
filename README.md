
# Contact Management System (Python)

A simple **command-line contact manager** written in Python.
Contacts are stored in a JSON file for persistence, allowing you to **add, remove, search, and display** contacts easily.



## Features

**Add a contact** (Name, Phone, Email)
**Remove a contact** by name
**Search** contacts (case-insensitive search)
**Show all contacts**
**Data persistence** using JSON storage

## Installation

1. **Clone this repository**

   ```bash
   git clone https://github.com/AlirezaRahi/Python-Contact-Management-System.git
   cd Python-Contact-Management-System
   ```

2. **Run the program**

   ```bash
   python contact_manager.py
   ```


## Usage

When you run the program, you’ll see a menu like this:

```
Contacts
1. Add a contact
2. Remove a contact
3. Search a contact
4. Show all contacts
5. Exit
```

* **Option 1:** Add a new contact
* **Option 2:** Remove a contact by name
* **Option 3:** Search for a contact
* **Option 4:** Display all saved contacts
* **Option 5:** Exit the program



## File Structure



├── contact_manager.py     # Main program
├── contact.json           # Contact data file (auto-created)
└── README.md              # Project documentation


## Example

**Adding a contact:**

```
name: John Doe
Tel: 123456789
email: john@example.com
Contact added: John Doe
```

**Searching a contact:**

```
Name: John Doe, Tel: 123456789, Email: john@example.com
```



## Requirements

* Python 3.x



## License

This project is licensed under the **MIT License**. - see the [LICENSE](LICENSE) file for details.


