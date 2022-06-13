#!/usr/bin/env python3
from email.headerregistry import Address
import subprocess
import sys
import socket
import sys

# Load the list of the hostnames
try:
    filepath = sys.argv[1]
except:
    print("You have to enter a path file, example: /home/lists.txt")
    sys.exit(1)
try:
    print("Reading file: ", filepath )
    my_file = open(filepath, "r")
    content = my_file.readlines()
except Exception as e:
    print("Cannot read file text, error message:", e )
    sys.exit(1)

# Resolving  and ping ip addresses of the hostnames
for i in content:
    try:
        ip = None
        ip = socket.gethostbyname(i.strip())
    except:
        ip = "Unknow, Cannot resolve"
    try:
        proc = None
        proc = subprocess.Popen(
        ['ping', '-q','-c', '1', i.strip()],
        stdout=subprocess.PIPE)
        stdout, stderr = proc.communicate()
        if proc.returncode == 0:
            pingresult = "success"
        else:
            pingresult = "failed"
    except Exception as e:
        pingresult = "Error: " + str(e)
    print("Name:", i.strip(), "Address: ", ip, "PingStatus: ", pingresult)
