#!/usr/bin/python
# Copyright (c) Younghwan Jang, 2014-2015
# You can copy, reuse, modify whatever you want but...
# I want you to specify where it is from.(It is not by force, but a recommendation)

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
