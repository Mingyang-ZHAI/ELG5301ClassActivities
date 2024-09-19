import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))
from phonebook.phonebook import PhoneBook

def main():
    phonebook = PhoneBook()

    # Import contacts from CSV
    phonebook.import_contacts_from_csv(os.path.join(os.path.dirname(__file__), 'test_contacts.csv'))
    # Update contacts to generate history
    phonebook.update_contact("John", "Doe", phone_number="(111) 222-3333")
    phonebook.update_contact("Jane", "Smith", address="789 Pine St")

    # View contact history
    contact = phonebook.view_contact("John", "Doe")
    if contact:
        print("History for John Doe:")
        history = contact.view_history()
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

    contact = phonebook.view_contact("Jane", "Smith")
    if contact:
        print("History for Jane Smith:")
        history = contact.view_history()
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

if __name__ == "__main__":
    main()