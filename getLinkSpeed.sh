#!/bin/sh
ethtool $1 | grep -i speed
