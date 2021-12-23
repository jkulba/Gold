#!/usr/bin/env python

import sys, os, random, string, time

"""
Reads files from specified directory.
:param LOG_DIR: directory location of log files
"""

#LOG_DIR = '/apps/ProFile/EXPORT/lock_manager/J/LSW'
LOG_DIR = '/home/jim/Projects/Gold/'

def main():
    print("Current working directory: ", LOG_DIR)

    if os.path.exists(LOG_DIR):
        os.chdir(LOG_DIR)

    read_file(LOG_DIR)

    pass

def read_file(LOG_DIR):
    for filename in os.listdir():
        path = os.path.join(LOG_DIR, filename)
        if os.path.isdir(path):
            continue
        print("FILENAME: " + filename)
        fd = os.open(filename, os.O_RDWR)
        fo = os.fdopen(fd, "r")
        os.lseek(fd, 0, 0)
        string = os.read(fd, 500)
        print("CONTENT")
        print(string)
        print(" ")
        print("Current I/O pointer position: %d" %fo.tell())
        fo.close()
        print("---------")

    print("Done")
    pass

if __name__=="__main__":
    main()
