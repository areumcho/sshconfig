import os.path
import sys

#checking ip address file and content validity
def ip_file_valid():


    #prompting user for input and save it into the var ip_file
    ip_file = input("\n# Enter IP file path and name eg(D:\MyApps\myfile.txt)")

    #Checking if the file exists (os.path is a method that is desgined to find if a file exists or not )
    if os.path.isfile(ip_file) == True:
        print("\n* IP file is valid :)\n")
    else:
        print("\n* File {} does not exist : ( Please check and try again. \n".format(ip_file))
        sys.exit()

    #Open user selected file for reading(IP addresses file)
    selected_ip_file = open(ip_file, 'r')

    #Starting from the beginning of the file using .seek method
    selected_ip_file.seek(0)

    #Reading each line (IP address) in the file
    ip_list = selected_ip_file.readlines()

    #Closing the file
    selected_ip_file.close()

    return ip_list


