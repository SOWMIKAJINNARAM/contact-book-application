# Contact Book Application

contacts = []

def show_menu():
    print("\n===== CONTACT BOOK MENU =====")
    print("1. Add Contact")
    print("2. View All Contacts")
    print("3. Search Contact")
    print("4. Update Contact")
    print("5. Delete Contact")
    print("6. Exit")

def add_contact():
    name = input("Enter Name: ")
    phone = input("Enter Phone Number: ")
    email = input("Enter Email: ")
    address = input("Enter Address: ")
    contacts.append({"name": name, "phone": phone, "email": email, "address": address})
    print("✅ Contact added successfully!")

def view_contacts():
    if not contacts:
        print("No contacts to display.")
    else:
        print("\n📋 Contact List:")
        for idx, contact in enumerate(contacts, start=1):
            print(f"{idx}. {contact['name']} - {contact['phone']}")

def search_contact():
    query = input("Enter name or phone to search: ").lower()
    found = False
    for contact in contacts:
        if query in contact['name'].lower() or query in contact['phone']:
            print("\n🔍 Contact Found:")
            print(f"Name   : {contact['name']}")
            print(f"Phone  : {contact['phone']}")
            print(f"Email  : {contact['email']}")
            print(f"Address: {contact['address']}")
            found = True
            break
    if not found:
        print("❌ No matching contact found.")

def update_contact():
    query = input("Enter name or phone of contact to update: ").lower()
    for contact in contacts:
        if query in contact['name'].lower() or query in contact['phone']:
            print("Enter new details (leave blank to keep existing):")
            new_name = input(f"Name [{contact['name']}]: ") or contact['name']
            new_phone = input(f"Phone [{contact['phone']}]: ") or contact['phone']
            new_email = input(f"Email [{contact['email']}]: ") or contact['email']
            new_address = input(f"Address [{contact['address']}]: ") or contact['address']
            contact.update({
                "name": new_name,
                "phone": new_phone,
                "email": new_email,
                "address": new_address
            })
            print("✅ Contact updated successfully!")
            return
    print("❌ No matching contact to update.")

def delete_contact():
    query = input("Enter name or phone of contact to delete: ").lower()
    for i, contact in enumerate(contacts):
        if query in contact['name'].lower() or query in contact['phone']:
            confirm = input(f"Are you sure you want to delete {contact['name']}? (y/n): ").lower()
            if confirm == 'y':
                contacts.pop(i)
                print("🗑️ Contact deleted.")
            else:
                print("Deletion canceled.")
            return
    print("❌ No matching contact to delete.")

# Main Loop
while True:
    show_menu()
    choice = input("Enter your choice (1-6): ")

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
        print("👋 Exiting Contact Book. Goodbye!")
        break
    else