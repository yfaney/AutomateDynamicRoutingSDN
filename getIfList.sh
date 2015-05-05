#!/bin/sh
# Copyright (c) Younghwan Jang, 2014-2015
# You can copy, reuse, modify whatever you want but...
# I want you to specify where it is from.(It is not by force, but a recommendation)

ifconfig -a | sed 's/[ \t].*//;/^\(lo\|\)\(s#\|\)$/d'
