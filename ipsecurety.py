import os
import subprocess

import getmac  # Library to get MAC address
from PyQt6.QtWidgets import QMessageBox

# Define the path for the MAC address file within the application's directory
APP_DIR = os.path.dirname(os.path.abspath(__file__))
MAC_FILE = os.path.join(APP_DIR, 'mac_address.txt')


def get_mac_address():
    command = "wmic csproduct get uuid"
    uuid = subprocess.check_output(command).decode().split("\n")[1].strip()
    return uuid


def store_mac_address(mac_address):
    # Write the MAC address to the text file
    with open(MAC_FILE, 'w') as file:
        file.write(mac_address)


def read_mac_address():
    # Read the MAC address from the text file
    if os.path.exists(MAC_FILE):
        with open(MAC_FILE, 'r') as file:
            return file.read().strip()
    return None


def decide():
    # Check if the stored MAC address matches the current MAC address
    stored_mac = read_mac_address()
    if stored_mac == "":
        store_mac_address(get_mac_address())
        return True
    elif stored_mac == get_mac_address():
        return True
    else:
        return False
