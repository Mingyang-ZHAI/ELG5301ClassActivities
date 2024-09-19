import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))
from phonebook.phonebook import PhoneBook

def test_import_contacts_from_csv():
    phonebook = PhoneBook()
    phonebook.import_contacts_from_csv('test_contacts.csv')
    contact = phonebook.view_contacts("first_name", "John")
    assert contact is not None, "Contact should be imported from CSV"
    print("test_import_contacts_from_csv passed")

if __name__ == "__main__":
    test_import_contacts_from_csv()