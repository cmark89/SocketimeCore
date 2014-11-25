#!/usr/bin/python

import socket
import sys

host = ""
port = 0

# Client program accepts up to 2 additional arguments
# Usage: client.py [HOST] [PORT]
# If host and port are not provided, it will default to local on
# port 5700

# Get the host to connect to
if len(sys.argv) >= 2:
	host = str(sys.argv[1])
else:
	host = socket.gethostname()	

# Get the port to connect to 
if len(sys.argv) >= 3:
	port = int(sys.argv[2])
else:
	port = 5700					
	
s = socket.socket()			# Create the socket
s.connect((host, port))		# Initiate a connection (using a tuple)

# Receive a message from the server and parse it to a string
print(s.recv(1024).decode('utf-8'))
print(s.recv(1024).decode('utf-8'))

s.close()					# Close when finished
