#!/usr/bin/env python

import sys, os, random, string, time

"""
Generates specified number of files with ASCII characters.
:param filename: unique filename
:param size: size in bytes
"""

NO_FILES = 500
FILE_SIZE = 500
LOG_DIR = '/apps/ProFile/EXPORT/lock_manager/J/LSW'

def main():
    print("Starting read log files")

    ROOT_DIR = os.getcwd()
    print("Current working directory: ", ROOT_DIR)

    if os.path.exists(ROOT_DIR):
        os.chdir(ROOT_DIR)

    read_file()

    pass

def read_file():
    for filename in os.listdir():
        print(filename)
        with open(filename) as fd:
            fo = os.fdopen(fd, "r")
            os.lseek(fd, 0, 0)
            string = os.read(fd, 500)
            print(string)
            print("Current I/O pointer position :%d" % fo.tell())
            fo.close()
    pass

if __name__=="__main__":
    main()
