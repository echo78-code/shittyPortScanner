#!/bin/python3

import sys #allows us to enter command line arguments, among other things
import socket
from datetime import datetime

#define our target
if len(sys.argv) == 2:
    target = socket.gethostbyname(sys.argv[1]) #translate a host name to IPv4
else:
    print('Invalid amount of arguments.')
    print('Syntax: python3 scanner.py <IP>')
    sys.exit()

#add a pretty banner
print('*' * 50)
print('scanning target ' + target)
print('time started: ' + str(datetime.now()))
print('*' *50)

try:
    for port in range(50,85):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket.setdefaulttimeout(1) #is a float
        result = s.connect_ex((target, port)) #return error indicator
        print('checking port {}'.format(port))
        if result == 0:
            print('{} port is open'.format(port))
        s.close()
except KeyboardInterrupt:
    print('\n exiting program.')
    sys.exit()

except socket.gaierror:
    print('hostname could not be resolved')
    sys.exit()

except socket.error:
    print('server not responding')
    sys.exit()