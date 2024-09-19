import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))
from phonebook.phonebook import PhoneBook

def test_delete_contact():
    phonebook = PhoneBook()
    phonebook.add_contact("Jane", "Smith", "(987) 654-3210", "jane.smith@example.com", "456 Elm St")
    phonebook.delete_contact("first_name", "Jane")
    contact = phonebook.view_contacts("first_name", "Jane")
    print (contact)
    assert len(contact) is 0, "Contact should be deleted"
    print("test_delete_contact passed")

if __name__ == "__main__":
    test_delete_contact()