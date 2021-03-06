import paramiko
import os.path
import time
import sys
import re


#check commands file
#prompt user for input - COMMANDS FILE
cmd_file =input("\n# Enter commands file path and name (e.g. D:\MyApps\myfile.txt): ")

#verify the validity of the COMMANDS FILE
if os.path.isfile(cmd_file) == True:
    print("\n* Command file is valid :)\n")
else:
    print("\n*  file {} does not exist :( Please check and try again.\n".format(cmd_file))
    sys.exit()


#open SSHv2 connection to the device
def ssh_connection(ip):

    #import a global variables from above
    #using the global keyword, can modify the variable inside the function
    global user_file
    global cmd_file

    #creating SSH CONNECTION
    try:
        #define SSH parameters
        #open the file for reading
        selected_user_file = open(user_file, 'r')

        #start from the beginning of the file
        selected_user_file.seek(0)

        #read username from the file
        username = selected_user_file.readlines()[0].split(',')[0].rstrip("\n")

        #start from the beginning of the file
        selected_user_file.seek(0)


        #read the passwd from the file
        password = selected_user_file.readline()[0].split(",")[1].rstrip("\n")


        #log into device
        session = paramiko.SSHClient()

        #can allow or deny host keys from unknown remote servers
        #!in production, never ever set it to autoaddpolicy!
        #do not forget to add this before actual connection to device
        session.set_missing_host_key_policy(paramiko.AutoAddPolicy())

        #connect to the device using uname and passwd
        session.connect(ip.rstrip("\n"), username=username, password=password)

        #start an interactive shell session on the router
        connection = session.invoke_shell()

        #set terminal length for entire output - disable pagination
        connection.send("endable\n")
        connection.send("terminal length 0\n")
        time.sleep(1)

        #enter global config mode
        connection.send("\n")
        connection.send("configure terminal\n")
        time.sleep(1)

        #open user selected file for reading
        selected_cmd_file = open(cmd_file, 'r')

        #read from the beginning
        selected_cmd_file.seek(0)

        #write each line in the file to the device
        for each_line in selected_cmd_file.readline():
            connection.send(each_line + '\n')
            time.sleep(2)

        #close the user file
        selected_user_file.close()

        #close the command file
        selected_cmd_file.close()

        #recieve 65535 bytes of data/output returned by the device to check IOS syntax error
        router_output = connection.recv(65535)

        #the b represents an instance of the bytes type, because the network device does not return plain text (type string) when querying it via SSH.
        if re.search(b"% Invalid input", router_output):
            print("* There was at least one IOS syntax error on device {}".format(ip))
        else:
            print("\nDONE for device {}".format(ip))

        #test for reading command output
        print(str(router_output) + "\n")


        #close the connection(session)
        session.close()

    except paramiko.AuthenticationException:
        print("* Invalid username or password \n*Please check the username/passwd")
        print("* closing the session...Bye!")














#paramiko - Python implementation of the SSHv2 protocol, providing both client and server functionality.
#paramiko is by far the most popular python module when it comes to remote network connections via paramiko
#paramiko needs to be installed since its not built in
#python -m pip install paramiko



