"""
This module defines the Contact class.
"""

import uuid
from datetime import datetime

class Contact:
    """
    A class to represent a contact entry in the phone book.

    Attributes:
    first_name (str): The first name of the contact.
    last_name (str): The last name of the contact.
    phone_number (str): The phone number of the contact.
    email (str, optional): The email address of the contact.
    address (str, optional): The address of the contact.
    created_time (datetime): The timestamp when the contact was created.
    updated_time (datetime): The timestamp when the contact was last updated.
    """
    
    def __init__(self, first_name, last_name, phone_number, email=None, address=None):
        """
        Initializes a new Contact instance.

        Parameters:
        first_name (str): The first name of the contact.
        last_name (str): The last name of the contact.
        phone_number (str): The phone number of the contact.
        email (str, optional): The email address of the contact.
        address (str, optional): The physical address of the contact.
        """
        self.id = uuid.uuid4()  # Generate a unique identifier for each contact
        self.first_name = first_name
        self.last_name = last_name
        self.phone_number = phone_number
        self.email = email
        self.address = address
        self.created_time = datetime.now()
        self.updated_time = datetime.now()
        self.history = []  # Initialize history log

    def update_contact(self, first_name=None, last_name=None, phone_number=None, email=None, address=None):
        """
        Updates the contact information and records the old data in the history log.

        Parameters:
        first_name (str, optional): The new first name of the contact.
        last_name (str, optional): The new last name of the contact.
        phone_number (str, optional): The new phone number of the contact.
        email (str, optional): The new email address of the contact.
        address (str, optional): The new physical address of the contact.
        """
        old_data = {
            'first_name': self.first_name,
            'last_name': self.last_name,
            'phone_number': self.phone_number,
            'email': self.email,
            'address': self.address,
            'created_time': self.created_time,
            'updated_time': self.updated_time
        }

        if first_name:
            self.first_name = first_name
        if last_name:
            self.last_name = last_name
        if phone_number:
            self.phone_number = phone_number
        if email:
            self.email = email
        if address:
            self.address = address

        # Make sure to update the updated_time
        self.updated_time = datetime.now()

        new_data = {
            'first_name': self.first_name,
            'last_name': self.last_name,
            'phone_number': self.phone_number,
            'email': self.email,
            'address': self.address,
            'created_time': self.created_time,
            'updated_time': self.updated_time
        }
        # Record the old data in the history log list
        self.history.append({
            'old_data': old_data,
            'new_data': new_data
        })
        print("Old data recorded:", old_data)  # Print the old data

    def view_history(self):
        """
        Returns the history of changes made to the contact.

        Returns:
        list: A list of dictionaries containing old data and timestamps.
        """
        return self.history
    