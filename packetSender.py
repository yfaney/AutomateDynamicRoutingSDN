#!/usr/bin/python

import sys
import socket               # Import socket module

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
port = 57777                # Reserve a port for your service.
PACKET = '1234567890ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnoprstuvwxyz!@#$%^&*()_+{}|[]:,.'

print sys.argv[1]
host = sys.argv[1]
s.connect((host, port))

while (True):
	s.send(PACKET)

s.close()
