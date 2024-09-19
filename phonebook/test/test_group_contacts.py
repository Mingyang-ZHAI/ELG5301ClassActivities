import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))
from phonebook.phonebook import PhoneBook

def test_group_contacts():
    phonebook = PhoneBook()
    phonebook.add_contact("John", "Doe", "(123) 456-7890", "john.doe@example.com", "123 Main St")
    phonebook.add_contact("Jane", "Smith", "(987) 654-3210", "jane.smith@example.com", "456 Elm St")
    grouped = phonebook.group_contacts()
    assert "D" in grouped and "S" in grouped, "Contacts should be grouped by last name"
    print("test_group_contacts passed")

if __name__ == "__main__":
    test_group_contacts()