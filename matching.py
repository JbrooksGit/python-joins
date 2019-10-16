#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 16 00:55:28 2019

@author: jonathanbrooks
"""

import csv

# load second file as lookup table
data = {}
with open("test.csv") as inf2:
    for row in csv.reader(inf2):
        data[row[0]] = row
        print(data)

# now process first file against it

with open("subjects.csv") as inf1:
    for row in csv.reader(inf1):
        if row[1] and row[2] and row[5] in data:
            print("hello")
