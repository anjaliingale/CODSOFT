class Contact:
    def __init__(self, name, phone, email, address):
        self.name = name
        self.phone = phone
        self.email = email
        self.address = address

    def __str__(self):
        return f"Name: {self.name}\nPhone: {self.phone}\nEmail: {self.email}\nAddress: {self.address}"

contacts = []

def add_contact():
    name = input("Enter the contact's name: ")
    phone = input("Enter the contact's phone number: ")
    email = input("Enter the contact's email address: ")
    address = input("Enter the contact's address: ")
    contact = Contact(name, phone, email, address)
    contacts.append(contact)
    print(f"Contact '{name}' added successfully!")

def view_contacts():
    if not contacts:
        print("No contacts found.")
    else:
        for i, contact in enumerate(contacts):
            print(f"\nContact {i + 1}:\n{contact}")

def search_contact(query):
    found = False
    for contact in contacts:
        if query.lower() in contact.name.lower() or query in contact.phone:
            print(contact)
            found = True
    if not found:
        print("No matching contacts found.")

def update_contact():
    query = input("Enter the name or phone number of the contact you want to update: ")
    found_contacts = []
    for contact in contacts:
        if query.lower() in contact.name.lower() or query in contact.phone:
            found_contacts.append(contact)
    if not found_contacts:
        print("No matching contacts found.")
    else:
        print("Matching contacts:")
        for i, contact in enumerate(found_contacts):
            print(f"{i + 1}. {contact.name}")
        
        choice = int(input("Enter the number of the contact you want to update: ")) - 1
        contact_to_update = found_contacts[choice]

        name = input("Enter the new name: ")
        phone = input("Enter the new phone number: ")
        email = input("Enter the new email address: ")
        address = input("Enter the new address: ")

        if name:
            contact_to_update.name = name
        if phone:
            contact_to_update.phone = phone
        if email:
            contact_to_update.email = email
        if address:
            contact_to_update.address = address

        print("Contact updated successfully!")

def delete_contact():
    query = input("Enter the name or phone number of the contact you want to delete: ")
    found_contacts = []
    for contact in contacts:
        if query.lower() in contact.name.lower() or query in contact.phone:
            found_contacts.append(contact)
    if not found_contacts:
        print("No matching contacts found.")
    else:
        print("Matching contacts:")
        for i, contact in enumerate(found_contacts):
            print(f"{i + 1}. {contact.name}")
        
        choice = int(input("Enter the number of the contact you want to delete: ")) - 1
        contact_to_delete = found_contacts[choice]

        contacts.remove(contact_to_delete)
        print(f"Contact '{contact_to_delete.name}' deleted successfully!")

while True:
    print("\nContact Book Menu:")
    print("1. Add Contact")
    print("2. View Contact List")
    print("3. Search Contact")
    print("4. Update Contact")
    print("5. Delete Contact")
    print("6. Exit")
    
    choice = input("Enter your choice (1/2/3/4/5/6): ")
    
    if choice == '1':
        add_contact()
    elif choice == '2':
        view_contacts()
    elif choice == '3':
        query = input("Enter the name or phone number to search for: ")
        search_contact(query)
    elif choice == '4':
        update_contact()
    elif choice == '5':
        delete_contact()
    elif choice == '6':
        print("Exiting Contact Book.")
        break
    else:
        print("Invalid choice. Please select a valid option.")
