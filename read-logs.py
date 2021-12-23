#!/usr/bin/env python

import sys, os, random, string, time

"""
Generates specified number of files with ASCII characters.
:param filename: unique filename
:param size: size in bytes
"""

NO_FILES = 500
FILE_SIZE = 500
#LOG_DIR = '/apps/ProFile/EXPORT/lock_manager/J/LSW'
LOG_DIR = '/home/jim/Projects/Gold/'

def main():
    print("Starting read log files")

    print("Current working directory: ", LOG_DIR)

    if os.path.exists(LOG_DIR):
        os.chdir(LOG_DIR)

    read_file(LOG_DIR)

    pass

def read_file(LOG_DIR):
    for root, dirs, files in os.walk('.', topdown=False, onerror=None, followlinks=False):
        for filename in files:
            print(os.path.join(LOG_DIR, filename))
            fd = os.open(filename, os.O_RDWR|os.O_CREAT)
            fo = os.fdopen(fd, "r")


    # for filename in os.listdir():
    #     print(filename)
    #     with open(filename) as fd:
    #         fo = os.fdopen(fd, "r")
    #         os.lseek(fd, 0, 0)
    #         string = os.read(fd, 500)
    #         print(string)
    #         print("Current I/O pointer position :%d" % fo.tell())
    #         fo.close()
    pass

if __name__=="__main__":
    main()
