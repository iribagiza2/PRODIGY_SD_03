contacts_file = "contacts.txt"

# Load contacts from file
def load_contacts():
    contacts = {}
    try:
        file = open(contacts_file, "r")
        for line in file:
            line = line.strip()
            if line:
                parts = line.split("|")
                name = parts[0]
                phone = parts[1]
                email = parts[2]
                contacts[name] = {"phone": phone, "email": email}
        file.close()
    except:
        pass  # no file exists yet
    return contacts

# Saving contacts to file
def save_contacts(contacts):
    file = open(contacts_file, "w")
    for name in contacts:
        phone = contacts[name]["phone"]
        email = contacts[name]["email"]
        line = name + "|" + phone + "|" + email + "\n"
        file.write(line)
    file.close()

# Adding a new contact
def add_contact(contacts):
    name = input("Enter name: ").strip()
    phone = input("Enter phone: ").strip()
    email = input("Enter email: ").strip()
    contacts[name] = {"phone": phone, "email": email}
    print("Contact added.")

# Viewing contacts
def view_contacts(contacts):
    if not contacts:
        print("No contacts yet.")
        return
    print("\nContact Lists:")
    for name in contacts:
        phone = contacts[name]["phone"]
        email = contacts[name]["email"]
        print("- " + name + ": " + phone + ", " + email)

# Editing a contact
def edit_contact(contacts):
    name = input("Enter name of contact to edit: ").strip()
    if name in contacts:
        phone = input("New phone (or leave blank to keep current): ").strip()
        email = input("New email (or leave blank to keep current): ").strip()
        if phone:
            contacts[name]['phone'] = phone
        if email:
            contacts[name]['email'] = email
        print("Contact updated.")
    else:
        print("Contact not found.")

# Deleting a contact
def delete_contact(contacts):
    name = input("Enter name of contact to delete: ").strip()
    if name in contacts:
        confirm = input("Are you sure you want to delete ", name, "? (yes/no): ").strip().lower()
        if confirm == 'yes':
            del contacts[name]
            print("Contact deleted.")
    else:
        print("Contact not found.")

# Main program loop
def main():
    contacts = load_contacts()

    while True:
        print("\n=== Contact Manager ===")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Edit Contact")
        print("4. Delete Contact")
        print("5. Exit")

        choice = input("Choose an option (1-5): ").strip()

        if choice == "1":
            add_contact(contacts)
        elif choice == "2":
            view_contacts(contacts)
        elif choice == "3":
            edit_contact(contacts)
        elif choice == "4":
            delete_contact(contacts)
        elif choice == "5":
            save_contacts(contacts)
            print("Contacts saved. Goodbye!")
            break
        else:
            print("Invalid choice.")

#Running the program
if __name__ == "__main__":
    main()
