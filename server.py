#!/usr/bin/python

""" This is a simple server demonstrating socket usage in Python."""

import socket
from datetime import datetime

logfile_name = "server.log"	# The name of the file to log connection data

def log_connection(addr):
	"""Save a record of the connection to the log"""
	with open(logfile_name, 'a') as file:
		file.write("%s - %s\n" % (str(datetime.now()), addr))

s = socket.socket()			# Create a socket

host = socket.gethostname()	# Get the local hostname
port = 5700					# Reserve a port number
s.bind((host,port))			# Bind the socket to the port using a tuple
s.listen(10)				# Begin listening for connections

# Loop to service the clients that connect
while True:
	c, addr = s.accept()	# This blocks until a connection comes in
	print("Receiving a connection from", addr)
	log_connection(addr)
	c.send(str.encode("Connected to server.\n"))
	c.send(str.encode("Server time: " + str(datetime.now())))
	c.close()
