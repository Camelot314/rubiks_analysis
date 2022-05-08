# code is not mine originally posted at
# https://www.javaer101.com/en/article/16819003.html

# Pass notebook file name in as argument when running. 
#  --> prints out number of lines of code in notebook 

#!/usr/bin/env python

from json import load
from sys import argv

def loc(nb):
    cells = load(open(nb))['cells']
    return sum(len(c['source']) for c in cells if c['cell_type'] == 'code')

def run(ipynb_files):
    return sum(loc(nb) for nb in ipynb_files)

if __name__ == '__main__':
    print(run(argv[1:]))