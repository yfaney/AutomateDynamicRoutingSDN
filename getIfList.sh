#!/bin/sh

ifconfig -a | sed 's/[ \t].*//;/^\(lo\|\)\(s#\|\)$/d'
