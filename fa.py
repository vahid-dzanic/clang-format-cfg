#!/usr/bin/python3

import glob 
#import _thread
import subprocess

def format(filename):
    subprocess.run(['clang-format', '-style=file', '-i', filename, '&'], stdout=subprocess.PIPE)


for filename in glob.iglob('./**/*.cpp', recursive=True):
    print(filename)
    format(filename)
    

for filename in glob.iglob('./**/*.h', recursive=True):
    print(filename)
    format(filename)

print('done')
exit(0)
