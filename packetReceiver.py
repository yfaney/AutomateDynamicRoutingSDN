#!/usr/bin/python           # This is server.py file

import socket               # Import socket module

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = ''
port = 57777                # Reserve a port for your service.
s.bind((host, port))        # Bind to the port

s.listen(10)                 # Now wait for client connection.
conn, addr = s.accept()
print 'Connected'
while True:
	data = conn.recv(1024)

c.close()                # Close the connection
