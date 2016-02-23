#!/usr/bin/python
#newsname-match.py

#Title:         NewsName Matcher
#Version:       1.0
#Author:        Sasan Bahadaran
#Date:          2/23/16
#Organization:  District Data Labs

##############################################
#   IMPORTS
##############################################
import os

#list of main candidates
candidates = ["Woodrow Wilson","Charles E. Hughes"]

path = './dates/19160101'

for filename in os.listdir(path):
    print filename
