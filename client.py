#!/usr/bin/python

import socket

s = socket.socket()			# Create the socket
host = socket.gethostname()	# Connecting locally for test purposes
port = 5700					# Get the port to connect to 

s.connect((host, port))		# Initiate a connection (using a tuple)

# Receive a message from the server and parse it to a string
print(s.recv(1024).decode('utf-8'))
print(s.recv(1024).decode('utf-8'))

s.close()					# Close when finished
