import json
import os

FILE_NAME = "contacts.json"

def load_contacts():
    """Load all contacts from JSON file."""
    if not os.path.exists(FILE_NAME):
        return []
    with open(FILE_NAME, "r", encoding="utf-8") as f:
        return json.load(f)

def save_contacts(contacts):
    """Save all contacts to JSON file."""
    with open(FILE_NAME, "w", encoding="utf-8") as f:
        json.dump(contacts, f, indent=4, ensure_ascii=False)

def add_contact(name, phone, email):
    """Add a new contact."""
    contacts = load_contacts()
    contacts.append({"name": name, "phone": phone, "email": email})
    save_contacts(contacts)
    print(f"Contact '{name}' has been added.")

def delete_contact(name):
    """Delete a contact by name."""
    contacts = load_contacts()
    updated_contacts = [c for c in contacts if c["name"].lower() != name.lower()]
    if len(updated_contacts) == len(contacts):
        print(f"No contact found with name '{name}'.")
    else:
        save_contacts(updated_contacts)
        print(f"Contact '{name}' has been deleted.")

def search_contacts(name):
    """Search for contacts by name (case-insensitive)."""
    contacts = load_contacts()
    results = [c for c in contacts if name.lower() in c["name"].lower()]
    if results:
        for c in results:
            print(f"Name: {c['name']}, Phone: {c['phone']}, Email: {c['email']}")
    else:
        print(f"No contacts found matching '{name}'.")

def show_all_contacts():
    """Display all saved contacts."""
    contacts = load_contacts()
    if contacts:
        for c in contacts:
            print(f"Name: {c['name']}, Phone: {c['phone']}, Email: {c['email']}")
    else:
        print("Contact list is empty.")

def main():
    """Main menu for contact manager."""
    while True:
        print("\n--- Contact Manager ---")
        print("1. Add a contact")
        print("2. Remove a contact")
        print("3. Search for a contact")
        print("4. Show all contacts")
        print("5. Exit")

        choice = input("Enter your choice: ").strip()

        if choice == "1":
            name = input("Name: ")
            phone = input("Phone: ")
            email = input("Email: ")
            add_contact(name, phone, email)
        elif choice == "2":
            name = input("Enter the name of the contact to delete: ")
            delete_contact(name)
        elif choice == "3":
            name = input("Enter the name to search for: ")
            search_contacts(name)
        elif choice == "4":
            show_all_contacts()
        elif choice == "5":
            print("Exiting Contact Manager...")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
