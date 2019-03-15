import paramiko
import os.path
import time
import sys
import re



# Checking commands file
# Prompting user for input - COMMANDS FILE
cmd_file =input("\n# Enter commands file path and name (e.g. D:\MyApps\myfile.txt): ")

# Verifying the validity of the COMMANDS FILE
if os.path.isfile(cmd_file) == True:
    print("\n* Command file is valid :)\n")
else:
    print("\n*  file {} does not exist :( Please check and try again.\n".format(cmd_file))
    sys.exit()


# Open SSHv2 connection to the device
def ssh_connection(ip):

    # Import a global variables from above
    # So using the global keyword, can modify the variable inside the function
    global user_file
    global cmd_file

    # Creating SSH CONNECTION
    try:
        # Define SSH parameters
        # opening the file for reading
        selected_user_file = open(user_file, 'r')

        # Starting from the beginning of the file



# Paramiko - Python implementation of the SSHv2 protocol, providing both client and server functionality.
# Paramiko is by far the most popular python module when it comes to remote network connections via paramiko
# Paramiko needs to be installed since its not built in
# python -m pip install paramiko



