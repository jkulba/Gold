#!/usr/bin/env python

import sys, os, random, string, time

"""
Generates specified number of files with ASCII characters.
:param filename: unique filename
:param size: size in bytes
"""

NO_FILES = 5
FILE_SIZE = 500

def main():
    print("Starting random file generator")

    ROOT_DIR = os.getcwd()
    print("Current working directory: ", ROOT_DIR)

    OUTPUT_DIR = str(random.randint(1000, 9999))
    if not os.path.exists(OUTPUT_DIR):
        os.makedirs(OUTPUT_DIR)
        os.chdir(OUTPUT_DIR)

    i = 1
    while i < NO_FILES:
        filename = str(random.randint(100,999)) + '.txt'    
        create_file(filename, FILE_SIZE)
        i += 1

    read_file()

    cleanup(ROOT_DIR, OUTPUT_DIR)
    pass

def create_file(filename, size):
    chars = ''.join([random.choice(string.ascii_letters) for i in range(size)])

    with open(filename, 'w') as f:
        f.write(chars)
    pass

def read_file():
    for root, dirs, files in os.walk('.', topdown=False, onerror=None, followlinks=True):
        for filename in files:
            print(filename)
            with open(filename) as f:
                print(f.readlines())
                f.close()
            time.sleep(1)
    pass

def check_python_version():
    print('Checking python version')
    if sys.version_info[0] > 2:
        raise Exception("Must be using Python 2")

def cleanup(ROOT_DIR, OUTPUT_DIR):
    print("Cleaning up output directory.")
    for root, dirs, files in os.walk('.', topdown=False, onerror=None, followlinks=True):
        for filename in files:
            os.remove(os.path.join(ROOT_DIR, OUTPUT_DIR, filename))        
    
    os.chdir(ROOT_DIR)
    if os.path.exists(OUTPUT_DIR):
        os.rmdir(OUTPUT_DIR)    
    pass

if __name__=="__main__":
    #check_python_version()
    main()
