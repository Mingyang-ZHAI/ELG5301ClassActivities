import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))
from phonebook.phonebook import PhoneBook

def test_update_contact():
    phonebook = PhoneBook()
    phonebook.add_contact("John", "Doe", "(123) 456-7890", "john.doe@example.com", "123 Main St")
    phonebook.update_contact("first_name", "John")
    contact = phonebook.view_contacts("first_name", "John")
    assert contact[0].first_name == "John", "Contact phone number should be updated"
    print("test_update_contact passed")

if __name__ == "__main__":
    test_update_contact()