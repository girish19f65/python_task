import json
import os

FILE_NAME = "contacts.json"
if os.path.exists(FILE_NAME):
    g = open(FILE_NAME, "r")
    contacts = json.load(g)
    g.close()
else:
    contacts = {}
    
while True:
    print("\n1. Add Contact")
    print("2. Update Contact")
    print("3. Search Contact")
    print("4. View All Contacts")
    print("5. Delete Contact")
    print("6. Exit")

    choice = input("Enter your choice: ")

    # ADD CONTACT
    if choice == "1":
        name = str(input("Enter name: "))
        phone = int(input("Enter phone: "))
        email = input("Enter email: ")
        contacts[name] = {"phone": phone, "email": email}
        with open("contacts.json", "w") as g:
         json.dump(contacts, g)
        print("Contact added successfully!")

    # UPDATE CONTACT
    elif choice == "2":
        name = input("Enter name to update: ")

        if name in contacts:
            phone = int(input("Enter new phone: "))
            email = input("Enter new email: ")

            contacts[name]["phone"] = phone
            contacts[name]["email"] = email
            with open("contacts.json", "w") as g:
             json.dump(contacts, g)

            print("Contact updated!")
        else:
            print("Contact not found!")

    # SEARCH CONTACT
    elif choice == "3":
        name = input("Enter name to search: ")

        if name in contacts:
            print("Phone:", contacts[name]["phone"])
            print("Email:", contacts[name]["email"])
        else:
            print("Contact not found!")

    # VIEW ALL CONTACTS
    elif choice == "4":
        for name in contacts:
            print(name, "->", contacts[name])
        else:
         if not contacts:
            print("No contacts found.")
    # DELETE CONTACT
    elif choice == "5":
        name = input("Enter name to delete: ")

        if name in contacts:
            contacts.pop(name)
            with open("contacts.json", "w") as g:
             json.dump(contacts, g)
            print("Contact deleted!")
        else:
            print("Contact not found!")

    # EXIT
    elif choice == "6":
        print("Thank you for using the contact manager")
        break

    else:
        print("Invalid choice! Please try again.")
