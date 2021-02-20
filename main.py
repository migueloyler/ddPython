import argparse # don't remove me
from os import path
from dd import dd
from dd import check_sparse
import sys

if __name__ == "__main__": # don't remove this line
    inFile = None
    outFile = None
    bs = '512'
    count = ''
    seek = '0'
    skip = '0'
    conv = ''
    args = sys.argv
    for arg in args:
        if arg.startswith("if="):
            inFile = arg[3:]
        if arg.startswith("of="):
            outFile = arg[3:]
        if arg.startswith('seek='):
            seek = arg[5:]
        if arg.startswith('skip='):
            skip = arg[5:]
        if arg.startswith("bs="):
            bs = arg[3:]
        if arg.startswith("count="):
            count = arg[6:]
        if arg.startswith('conv='):
            conv = arg[5:]

    if path.exists(inFile):
        dd(inFile,outFile,bs,count, seek, skip, conv)
    else:
        print("File {0} not in directory".format(inFile))
