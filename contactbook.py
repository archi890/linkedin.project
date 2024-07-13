# Initialize an empty list to store contacts
contacts = []

# Function to add a new contact
def add_contact():
    name = input("Enter the contact's name: ")
    phone = input("Enter the contact's phone number: ")
    email = input("Enter the contact's email address: ")
    address = input("Enter the contact's address: ")
    
    contact = {
        'Name': name,
        'Phone': phone,
        'Email': email,
        'Address': address
    }
    
    contacts.append(contact)
    print("Contact added successfully!")

# Function to display all contacts
def view_contacts():
    if not contacts:
        print("No contacts found.")
    else:
        print("Contact List:")
        for index, contact in enumerate(contacts, start=1):
            print(f"{index}. Name: {contact['Name']}, Phone: {contact['Phone']}")

# Function to search for a contact by name or phone number
def search_contact():
    search_term = input("Enter the name or phone number to search: ")
    found_contacts = []
    
    for contact in contacts:
        if search_term in contact['Name'] or search_term in contact['Phone']:
            found_contacts.append(contact)
    
    if not found_contacts:
        print("No matching contacts found.")
    else:
        print("Matching Contacts:")
        for contact in found_contacts:
            print(f"Name: {contact['Name']}, Phone: {contact['Phone']}")

# Function to update a contact
def update_contact():
    view_contacts()
    index = int(input("Enter the index of the contact to update: ")) - 1
    
    if index < 0 or index >= len(contacts):
        print("Invalid index.")
    else:
        updated_name = input("Enter the updated name (leave empty to keep it unchanged): ")
        updated_phone = input("Enter the updated phone number (leave empty to keep it unchanged): ")
        updated_email = input("Enter the updated email address (leave empty to keep it unchanged): ")
        updated_address = input("Enter the updated address (leave empty to keep it unchanged): ")
        
        if updated_name:
            contacts[index]['Name'] = updated_name
        if updated_phone:
            contacts[index]['Phone'] = updated_phone
        if updated_email:
            contacts[index]['Email'] = updated_email
        if updated_address:
            contacts[index]['Address'] = updated_address
        
        print("Contact updated successfully!")

# Function to delete a contact
def delete_contact():
    view_contacts()
    index = int(input("Enter the index of the contact to delete: ")) - 1
    
    if index < 0 or index >= len(contacts):
        print("Invalid index.")
    else:
        deleted_contact = contacts.pop(index)
        print(f"Contact '{deleted_contact['Name']}' deleted successfully!")

# Main menu
while True:
    print("\nContact Management System")
    print("1. Add Contact")
    print("2. View Contacts")
    print("3. Search Contact")
    print("4. Update Contact")
    print("5. Delete Contact")
    print("6. Quit")
    
    choice = input("Enter your choice (1/2/3/4/5/6): ")
    
    if choice == '1':
        add_contact()
    elif choice == '2':
        view_contacts()
    elif choice == '3':
        search_contact()
    elif choice == '4':
        update_contact()
    elif choice == '5':
        delete_contact()
    elif choice == '6':
        print("Goodbye!")
        break
    else:
        print("Invalid choice. Please try again.")