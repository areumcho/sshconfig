#sys module provides information about constants, functions and methods of the Python interpreter.
import sys


"""

Loopback: 127.0.0.0 - 127.255.255.255
Multicast: 224.0.0.0 - 239.255.255.255
Boradcast: 255.255.255.255
Link-Local: 169.254.0.0 - 169.254.255.255
Reserved for future use: 240.0.0.0-255.255.255.254

"""

def ip_addr_valid(list):
    for ip in list:
        ip = ip.rstrip("\n")
        #ip.rstrip - The rstrip() method removes any trailing characters (characters at the end a string), space is the default trailing character to remove.
        # we are getting rid of '\n' keep just the ip address
        #['10.10.10.2\n', '10.10.10.3\n', '10.10.10.4\n']
        octet_list = ip.split(".")

        # it it meets the conditions below then if should operate the code inside.
        
        if (len(octet_list) == 4) and (1<= int(octet_list[0] <=223) and (int(octet_list[0]) !=127) and (int(octet_list[0]) != 169) or int(octet_list[1]) !=254 and (0 <=int(octet_list[1]) <= 255) and 0<= int(octet_list[2]) <= 255 and 0 <=int(octet_list[3]) <=255):
            continue
        else:
            print()
            sys.exit()



"""
# Again set the pointer to the beginning
a.seek(0)


1. (len(octet_list) == 4) - it should have 4 octets
2. (1<= int(octet_list[0] <= 223) - excluding multicast range
3. (int(octet_list[0]) !=127 - excludinig loopback
4. (int(octet_list[0]) != 169 -  first octet should not be 169 excluding link-local
5.  int(octet_list[1]) !=254 - second octet should not be 254
"""

