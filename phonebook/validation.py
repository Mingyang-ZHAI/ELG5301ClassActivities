# phonebook/validation.py

"""
This module defines validation functions for the Phone Book Management Application.
"""

import re
from typing import Optional


def validate_phone_number(phone_number: Optional[str]) -> bool:
    """
    Validates the phone number format.

    Parameters:
    phone_number (str): The phone number to validate.

    Returns:
    bool: True if the phone number is valid, False otherwise.
    """
    pattern = re.compile(r'^(\(\d{3}\) \d{3}-\d{4}|\d{10})$')
    return pattern.match(phone_number) is not None


def validate_email(email: Optional[str]) -> bool:
    """
    Validates the email address format.

    Parameters:
    email (str): The email address to validate.

    Returns:
    bool: True if the email address is valid, False otherwise.
    """
    pattern = re.compile(r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$')
    return pattern.match(email) is not None
