import sys
import subprocess
# Checking IP reachability


def ip_reach(list):
    for ip in list:
        ip = ip.rstrip("\n")

# ping each device using call method = Run the command described by args. Wait for command to complete, then return the returncode attribute.
        ping_reply = subprocess.call('ping %s /n 2' % (ip), stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

# 0 means that the ping was successful and the device is reachable, By linux standard 0==success
        if ping_reply == 0:
            print("\n* {} is reachable :)\n".format(ip))
            continue
        else:
            print('\n* {} not reachable :{  chack connectivity and try again.'.foramt(ip))
            sys.exit()

# 'ping %s /n 2' % (ip), ping cammand + %s string format operator
# %(ip) single argument
# 2 more argument stdout=subprocess.DEVNULL Err => so they dont want any msg genrated by ping commands
# eg no request time out, host unreachable kind of msgs
# stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
# The format() method returns the formatted string.
