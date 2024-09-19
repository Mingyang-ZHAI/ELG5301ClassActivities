# Your code should be thoroughly documented, featuring docstrings for functions and comments that elucidate complex code sections.

# Advanced Phone Book Management Application

## Overview

This is a command-line Python app to manage contacts. It lets users create, view, search, update, and delete contacts. The app supports advanced features like search, input validation, sorting, grouping, logging, and more.


## Features

### 1. Basic Operations

Users can perform these operations:

	•	Create: Add new contacts one at a time or in bulk using a CSV file.
	•	Retrieve: Search and view contacts by name or phone number.
	•	Update: Modify existing contact details.
	•	Delete: Remove contacts one by one or in batches.


### 2. Advanced Search

	•	Wildcard Search: Search for partial matches in names or phone numbers.
	•	Time Filter: Find contacts added during a specific time period.


### 3. Sorting and Grouping

	•	Sort Alphabetically: Sort contacts by first or last name.
	•	Group by Initial: Group contacts by the first letter of the last name.


### 4. Logging and Auditing

	•	Action Logging: Logs every action (create, update, delete) with timestamps.
	•	Change History: Shows the full history of changes for each contact.


### 5. Input Validation

	•	Phone Numbers: Validates numbers using the format (###) ###-####.
	•	Email Validation: Checks for valid email addresses.


---

## Code Structure

### 1. Contact Class

Represents a contact entry with:

	•	Attributes: First Name, Last Name, Phone Number, Email, Address, Created Time, Updated Time.
	•	Methods: For creating, updating, and managing contact info.只有 update


### 2. PhoneBook Class

Manages the contact list and handles all CRUD operations:

	•	Methods:
	•	add_contact(): Add new contacts (individually or from a CSV).
	•	view_contact(): Retrieve contact details.
	•	update_contact(): Update existing contacts.
	•	delete_contact(): Remove contacts.
	•	search_contact(): Search contacts with wildcards and filters.
	•	sort_contacts(): Sort contacts alphabetically.
	•	group_contacts(): Group contacts by the first letter of the last name.


### 3. CLI Script

The command-line interface script provides the user with:
This script allows users to:

	•	Input Prompts: For adding, viewing, searching, updating, and deleting contacts.
	•	Error Handling: Catches invalid inputs and displays user-friendly error messages.
	•	Validate Input: Ensures valid phone numbers and email addresses.


### 4. Logging and Auditing System

Logs user actions in a file, including:

	•	Action: What was done (create, update, delete).
	•	Timestamp: When the action happened.
	•	Affected Contact: Details of the contact involved in the operation.

---

## Testing

Testing

The app was tested under various scenarios:

	1.	Adding Contacts: Tested with valid and invalid inputs, single and batch inputs.
	2.	Searching Contacts: Tested wildcard searches and filters for different time ranges.
	3.	Updating Contacts: Verified that updates are logged and changes reflect correctly.
	4.	Deleting Contacts: Tested both individual and batch deletions.
	5.	Sorting and Grouping: Tested correct sorting and grouping of contacts.
	6.	Error Handling: Made sure the app catches invalid inputs and shows clear messages.
---

## How to Use

1. Installation

First, install Python 3, clone the repository, and navigate to the project folder.

2. Run the App

Start the app with this command:

```
python3 -m phonebook.cli
```

