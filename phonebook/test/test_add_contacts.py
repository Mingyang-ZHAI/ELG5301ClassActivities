import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))
from phonebook.phonebook import PhoneBook

def test_add_contact():
    phonebook = PhoneBook()
    phonebook.add_contact("John", "Doe", "(123) 456-7890", "john.doe@example.com", "123 Main St")
    contact = phonebook.view_contacts("first_name", "John")
    assert contact is not None, "Contact should be added"
    print("test_add_contact passed")

if __name__ == "__main__":
    test_add_contact()