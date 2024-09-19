import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))
from phonebook.phonebook import PhoneBook
from phonebook.contact import Contact

def test_view_contact_history():
    phonebook = PhoneBook()
    phonebook.add_contact("John", "Doe", "(123) 456-7890", "john.doe@example.com", "123 Main St")
    phonebook.update_contact("first_name", "John")
    contacts = phonebook.view_contacts("first_name", "John")
    contact = contacts[0] if contacts else None
    history = contact.view_history() if contact else []
    assert len(history) > 0, "Contact history should be viewable"
    print("test_view_contact_history passed")

if __name__ == "__main__":
    test_view_contact_history()