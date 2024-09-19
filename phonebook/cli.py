# phonebook/cli.py

"""
This module defines the command-line interface for the Phone Book Management Application.
"""

import sys
from phonebook.phonebook import PhoneBook
from phonebook.contact import Contact

def main():
    """
    The main function to run the command-line interface.
    """
    phonebook = PhoneBook()

    while True:
        print("\nPhone Book Manager")
        print("1. Add Contact")
        print("2. View Contact")
        print("3. Update Contact")
        print("4. Delete Contact")
        print("5. Search Contacts")
        print("6. Sort Contacts")
        print("7. Group Contacts")
        print("8. Import Contacts from CSV")
        print("9. View Contact History")
        print("10. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            first_name = input("First Name: ")
            last_name = input("Last Name: ")
            phone_number = input("Phone Number: ")
            email = input("Email (Optional): ")
            address = input("Address (Optional): ")
            phonebook.add_contact(first_name, last_name, phone_number, email, address)
        elif choice == '2':
            aim_type = input("Search by (first_name, last_name, phone_number, email, address): ")
            aim_term = input(f"Enter {aim_type}: ")
            contact_results = phonebook.view_contacts(aim_type, aim_term)
            if contact_results:
                for contact in contact_results:
                    print(f"Name: {contact.first_name} {contact.last_name}")
                    print(f"Phone Number: {contact.phone_number}")
                    print(f"Email: {contact.email}")
                    print(f"Address: {contact.address}")
                    print(f"Created Time: {contact.created_time}")
                    print(f"Updated Time: {contact.updated_time}")
                    print("-" * 20)
            else:
                print("Contact not found.")
        elif choice == '3':
            aim_type = input("Search by (first_name, last_name, phone_number, email, address): ")
            aim_term = input(f"Enter old {aim_type}: ")
            first_name = input("New First Name (Optional): ")
            last_name = input("New Last Name (Optional): ")
            phone_number = input("New Phone Number (Optional): ")
            email = input("New Email (Optional): ")
            address = input("New Address (Optional): ")
            phonebook.update_contact(aim_type, aim_term, first_name, last_name, phone_number, email, address)
        elif choice == '4':
            aim_type = input("Search by (first_name, last_name, phone_number, email, address): ")
            aim_term = input(f"Enter the contract content you want to delete: ")
            phonebook.delete_contact(aim_type, aim_term)
            print("Contact(s) deleted.")

        elif choice == '5':
            results = []
            search_by = input("Search by (contract_content, time): ")
            if search_by == 'contract_content':
                aim_term = input(f"Enter the contract content you want to search: ")
                results = phonebook.search_contact(aim_term=aim_term)
            elif search_by == 'time':
                start_date = input("Enter start date (YYYYMMDD): ")
                end_date = input("Enter end date (YYYYMMDD): ")
                results = phonebook.search_contact(start_date=start_date, end_date=end_date)
            else:
                print("Invalid search type.")
        elif choice == '6':
            field = input("Sort by (first_name, last_name, phone_number, email, address): ")
            phonebook.sort_contacts(field)
            print("Contacts sorted.")
        elif choice == '7':
            field = input("Group by (first_name, last_name, phone_number, email, address): ")
            grouped = phonebook.group_contacts(field)
            for initial, contacts in grouped.items():
                print(f"{initial}:")
                for contact in contacts:
                    print(f"  {contact.first_name} {contact.last_name}")
        elif choice == '8':
            file_path = input("Enter CSV file path: ")
            phonebook.import_contacts_from_csv(file_path)
            print("Contacts imported from CSV.")
        elif choice == '9':
            aim_type = input("Search by (first_name, last_name, phone_number, email, address): ")
            aim_term = input(f"Enter {aim_type}: ")
            contact_results = phonebook.view_contacts(aim_type, aim_term)
            if contact_results:
                for contact in contact_results:
                    history = contact.view_history()
                    print(f"History for {contact.first_name} {contact.last_name}:")
                    for record in history:
                        print(f"Old Data Timestamp: {record['old_data']['timestamp']}")
                        print(f"  First Name: {record['old_data']['first_name']}")
                        print(f"  Last Name: {record['old_data']['last_name']}")
                        print(f"  Phone Number: {record['old_data']['phone_number']}")
                        print(f"  Email: {record['old_data']['email']}")
                        print(f"  Address: {record['old_data']['address']}")
                        print(f"New Data Timestamp: {record['new_data']['timestamp']}")
                        print(f"  First Name: {record['new_data']['first_name']}")
                        print(f"  Last Name: {record['new_data']['last_name']}")
                        print(f"  Phone Number: {record['new_data']['phone_number']}")
                        print(f"  Email: {record['new_data']['email']}")
                        print(f"  Address: {record['new_data']['address']}")
                        print("-" * 20)
            else:
                print("Contact not found.")
        elif choice == '10':
            sys.exit()
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
