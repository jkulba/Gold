#!/usr/bin/env python

import sys, os, random, string

"""
Generates specified number of files with ASCII characters.
:param filename: unique filename
:param size: size in bytes
"""

NO_FILES = 5
FILE_SIZE = 500
DIR_NAME = ""

def main():
    print("Starting random file generator")

    i = 1
    while i < NO_FILES:
        filename = str(random.randint(100,999)) + '.txt'
        
        create_file(filename, FILE_SIZE)
        i += 1

def create_file(filename, size):
    chars = ''.join([random.choice(string.ascii_letters) for i in range(size)])

    with open(filename, 'w') as f:
        f.write(chars)
    pass

def check_python_version():
    print('Checking python version')
    if sys.version_info[0] > 2:
        raise Exception("Must be using Python 2")

def cleanup(dirname):
    pass

if __name__=="__main__":
    #check_python_version()
    main()
