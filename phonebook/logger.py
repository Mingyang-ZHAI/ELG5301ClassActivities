import logging
import os

# Define the path for the log file
log_dir = os.path.join(os.path.dirname(__file__), '..', 'phonebook')
log_file_path = os.path.join(log_dir, 'phonebook.log')

# Ensure the log directory exists
os.makedirs(log_dir, exist_ok=True)

# Set up logging
logging.basicConfig(
    filename=log_file_path,
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S'  # This defines the timestamp format
)

def log_info(message):
    """Logs an info message."""
    logging.info(message)