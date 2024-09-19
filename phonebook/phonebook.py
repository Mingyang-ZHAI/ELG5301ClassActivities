"""
This module defines the PhoneBook class for managing contacts.
"""

import csv
from datetime import datetime
from phonebook.contact import Contact
from phonebook.validation import validate_email, validate_phone_number
from phonebook.logger import log_info

class PhoneBook:
    """
    A class to manage the contact list and handles all CRUD operations:
    create, read, update, and delete.
    """

    def __init__(self):
        """
        Initializes a new PhoneBook instance.
        """
        self.contacts = []

    def add_contact(self, first_name, last_name, phone_number, email=None, address=None):
        """
        Creates a new contact and adds it to the phone book.

        Parameters:
        first_name (str): The first name of the contact.
        last_name (str): The last name of the contact.
        phone_number (str): The phone number of the contact.
        email (str, optional): The email address of the contact.
        address (str, optional): The address of the contact.
        """
        # Make sure to verfiy the phone number is valid
        if not validate_phone_number(phone_number):
            raise ValueError("Invalid phone number, please use the format (xxx) xxx-xxxx")
        
        # Make sure to verfiy the email is valid
        if email and not validate_email(email):
            raise ValueError("Invalid email address")
        
        # Then we can add a new contact
        contact = Contact(first_name, last_name, phone_number, email, address)
        self.contacts.append(contact)
        log_content = "Added contact: {} {} | Phone: {} | Email: {} | Address: {}".format(
                contact.first_name,
                contact.last_name,
                contact.phone_number,
                contact.email or 'N/A',
                contact.address or 'N/A'
            )
        log_info(log_content)
        print(log_content)
        
    def import_contacts_from_csv(self, file_path):
        """
        Imports contacts from a CSV file.

        Parameters:
        file_path (str): The path to the CSV file.
        """
        with open(file_path, mode='r') as file:
            csv_reader = csv.DictReader(file)
            for row in csv_reader:
                self.add_contact(row['First Name'], row['Last Name'], row['Phone Number'], row.get('Email'), row.get('Address'))
            log_info(f"Imported contacts from {file_path}")

    def view_contacts(self, aim_type, aim_term):
        """
        Retrieves a contact by search_type.

        Parameters:
        aim_type (str): The type of the contact to deal with.
        aim_term (str): The value of the contact to deal with.
        """
        search_map = {
            'first_name': lambda contact: contact.first_name,
            'last_name': lambda contact: contact.last_name,
            'phone_number': lambda contact: contact.phone_number,
            'email': lambda contact: contact.email,
            'address': lambda contact: contact.address
        }

        results = []
        for contact in self.contacts:
            if aim_type in search_map and search_map[aim_type](contact) == aim_term:
                log_content = "Searched contact: {} {} | Phone: {} | Email: {} | Address: {}".format(
                    contact.first_name,
                    contact.last_name,
                    contact.phone_number,
                    contact.email or 'N/A',
                    contact.address or 'N/A'
                )
                log_info(log_content)
                print(log_content)
                results.append(contact)
        if not results:
            print("No contacts found.")
        return results

    def update_contact(self, aim_type, aim_term, first_name=None, last_name=None, phone_number=None, email=None, address=None):
        """
        Updates an existing contact.

        Parameters:
        aim_type (str): The type of the contact to deal with.
        aim_term (str): The value of the contact to deal with.
        """
        old_contacts = self.view_contacts(aim_type, aim_term)
        if old_contacts:
            for old_contact in old_contacts:

                # save the old data to history
                old_data = {
                    'first_name': old_contact.first_name,
                    'last_name': old_contact.last_name,
                    'phone_number': old_contact.phone_number,
                    'email': old_contact.email,
                    'address': old_contact.address,
                    'created_time': old_contact.created_time,
                    'updated_time': old_contact.updated_time
                }
                if first_name:
                    old_contact.first_name = first_name
                if last_name:
                    old_contact.last_name = last_name
                if phone_number:
                    old_contact.phone_number = phone_number
                if email:
                    old_contact.email = email
                if address:
                    old_contact.address = address
                old_contact.updated_time = datetime.now()
                log_content = "Updated contact: {} {} | Phone: {} | Email: {} | Address: {}".format(
                    old_contact.first_name,
                    old_contact.last_name,
                    old_contact.phone_number,
                    old_contact.email or 'N/A',
                    old_contact.address or 'N/A'
                )

                new_data = {
                    'first_name': old_contact.first_name,
                    'last_name': old_contact.last_name,
                    'phone_number': old_contact.phone_number,
                    'email': old_contact.email,
                    'address': old_contact.address,
                    'created_time': old_contact.created_time,
                    'updated_time': old_contact.updated_time
                }
                # Record the old data in the history log list
                old_contact.history.append({
                    'old_data': old_data,
                    'new_data': new_data
                })
                print("Old data recorded:", old_data)  # Print the old data
                log_info(log_content)
                print(log_content)
        else:
            log_info("Contact not found, cannot update")
            raise ValueError("Contact not found, cannot update")
            
    def delete_contact(self, aim_type, aim_term):
        """
        Deletes an existing contact.

        Parameters:
        aim_type (str): The type of the contact to deal with.
        aim_term (str): The value of the contact to deal with.
        """
        old_contacts = self.view_contacts(aim_type, aim_term)
        if old_contacts:
            for old_contact in old_contacts:
                self.contacts.remove(old_contact)
            log_info("Deleted contact: {} {} | Phone: {} | Email: {} | Address: {}".format(
                old_contact.first_name,
                old_contact.last_name,
                old_contact.phone_number,
                old_contact.email or 'N/A',
                old_contact.address or 'N/A'
            ))
        else:
            log_info("Contact not found, cannot delete")
            raise ValueError("Contact not found, cannot delete")

    def sort_contacts(self, aim_type='last_name'):
        """
        Sorts the contacts alphabetically by the aim_type.

        Parameters:
        aim_type (str): The type of the contact to deal with.
        """
        self.contacts.sort(key=lambda contact: getattr(contact, aim_type))
        log_info(f"Contacts sorted by {aim_type}")
        for contact in self.contacts:
            print("Sorted contact: {} {} | Phone: {} | Email: {} | Address: {}".format(
                contact.first_name,
                contact.last_name,
                contact.phone_number,
                contact.email or 'N/A',
                contact.address or 'N/A'
            ))

    def group_contacts(self, aim_type='last_name'):
        """
        Groups contacts by the initial letter of the aim_type.

        Parameters:
        aim_type (str): The type of the contact to deal with.

        Returns:
        dict: A dictionary with initials as keys and lists of Contact instances as values.
        """
        grouped = {}
        for contact in self.contacts:
            initial = getattr(contact, aim_type)[0].upper()
            if initial not in grouped:
                grouped[initial] = []
            grouped[initial].append(contact)
        
        log_info(f"Contacts grouped by {aim_type}")
        for initial, contacts in grouped.items():
            print(f"Group {initial}:")
            for contact in contacts:
                print("Grouped contact: {} {} | Phone: {} | Email: {} | Address: {}".format(
                    contact.first_name,
                    contact.last_name,
                    contact.phone_number,
                    contact.email or 'N/A',
                    contact.address or 'N/A'
                ))
        return grouped

    def search_contact(self, aim_term=None, start_date=None, end_date=None):
        """
        Search for contacts using partial match (wildcard) or time frame filter.

        Parameters:
        aim_term (str): Partial search string for first name, last name, phone number, email, or address
        start_date: Start of the time frame filter (YYYY-MM-DD)
        end_date: End of the time frame filter (YYYY-MM-DD)
        
        Returns:
        List of matching contacts
        """
        results = []

        for contact in self.contacts:
            # Wildcard search: Match aim_term with first_name, last_name, phone_number, email, or address
            if aim_term and (
                aim_term.lower() in contact.first_name.lower() or
                aim_term.lower() in contact.last_name.lower() or
                aim_term in contact.phone_number or
                (contact.email and aim_term.lower() in contact.email.lower()) or
                (contact.address and aim_term.lower() in contact.address.lower())
            ):
                results.append(contact)

            # Time frame filter: Match contacts created within a date range
            if start_date and end_date:
                try:
                    start_dt = datetime.strptime(start_date, "%Y%m%d")
                    end_dt = datetime.strptime(end_date, "%Y%m%d")
                    if hasattr(contact, 'created_time') and start_dt <= contact.created_time <= end_dt:
                        results.append(contact)
                except ValueError:
                    print("Invalid date format. Please use YYYYMMDD.")
                    return []

        if not results:
            print("No contacts found.")
        else:
            for contact in results:
                print("searched contact: {} {} | Phone: {} | Email: {} | Address: {}".format(
                    contact.first_name,
                    contact.last_name,
                    contact.phone_number,
                    contact.email or 'N/A',
                    contact.address or 'N/A'
                ))
        return results
