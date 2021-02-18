import math
import os.path
from os import path
import sys

def check_sparse(blk):
    for i in blk:
        if i != 0:
            return False
    return True


def dd(inFile, outFile, bs = '512', count = '', seek = '0', skip = '0', conv=''):
    if 'lcase' in conv and 'ucase' in conv:
        print('illegal combination')
        return
    suffix = {'c': 1, 'w':2, 'b':512, 'kB':1000, 'K': 1024, 'MB': 1000*1000, 
    'M': 1024*1024, 'xM':1024*1024, 'GB':1000*1000*1000, 'G': 1024*1024*1024,
    'KiB':1024, 'MiB':1024*1024, 'GiB':1024*1024*1024}
    op_arr = ['KiB', 'MiB', 'GiB', 'kB', 'xM', 'GB', 'MB', 'c', 'w', 'b', 'K', 'M', 'G']
    no_prefix_flag = 1
    for i in op_arr:
        if i in bs:
            l = len(i)
            num = bs[:-l]
            bs = int(num) * suffix[i]
            no_prefix_flag = 0
            break
    if no_prefix_flag == 1:
        bs = int(bs)
    else:
        no_prefix_flag = 1

    for i in op_arr:
        if i in  count:
            l = len(i)
            num = count[:-l]
            count = int(num) * suffix[i]
            no_prefix_flag = 0
            break
    if no_prefix_flag == 1:
        if count == '':
            count = sys.maxsize
        else:
            count = int(count)
    else:
        no_prefix_flag = 1

    
    for i in op_arr:
        if i in seek:
            l = len(i)
            num = seek[:-l]
            seek = int(num) * suffix[i] * bs
            no_prefix_flag = 0
            break
    if no_prefix_flag == 1:
        seek = int(seek) * bs
    else:
        no_prefix_flag = 1

    for i in op_arr:
        if i in skip:
            l = len(i)
            num = bs[:-l]
            skip = int(num) * suffix[i] * bs
            no_prefix_flag = 0
            break
    if no_prefix_flag == 1:
        skip = int(skip) * bs
    else:
        no_prefix_flag = 1


    to_copy = bytearray()

    if path.exists(outFile):
        with open(outFile, 'rb') as oFile:
            f = oFile.read()
            file_lengh = len(f)
        with open(outFile, 'rb') as oFile:
            if seek > file_lengh:
                seek_buffer = seek - file_lengh
                buff = bytearray(seek_buffer)
                f = oFile.read()
                for i in f:
                    to_copy.append(i)
                for i in buff:
                    to_copy.append(i)
            else:
                f = oFile.read(seek)
                for i in f:
                    to_copy.append(i)
    else:
        buff = bytearray(seek)
        for i in buff:
            to_copy.append(bytes(i))
    
    with open(inFile, 'rb') as iFile:
        f = iFile.read(skip)
        f = iFile.read(bs)
        while f and count != 0:
            if 'sparse' in conv:
                if check_sparse(f):
                    f = iFile.read(bs)
                    continue
            for byte in f:
                to_copy.append(byte)
            count -= 1
            f = iFile.read(bs)

    if path.exists(outFile):
        os.remove(outFile)

    #p = bytes(to_copy) 

    with open(outFile, 'wb') as out:
        cnt = 0
        z = []
        for i in bytes(to_copy):
            if 'ucase' in conv:
                if i >= 32 and i<=127:
                    to_convert = chr(i)
                    to_convert = to_convert.upper()
                    to_convert = ord(to_convert)
                    out.write(bytes([to_convert]))
                    continue
            elif 'lcase' in conv:
                if i >= 32 and i<=127:
                    to_convert = chr(i)
                    to_convert = to_convert.lower()
                    to_convert = ord(to_convert)
                    out.write(bytes([to_convert]))
                    continue
            else:
                out.write(bytes([i]))
                z.append(i)
            cnt+=1
        #a = 11

        #with open(outFile, 'rb') as o:
        #    f = o.read()
        #    a = 11



#dd('in.txt', "out.txt", count='1', seek='4')


    
'''    
def is_printable(s):
    output = ""
    for c in s:
        if c >= 32 and c <= 127:
            output += chr(c)
        else:
            output += "."
    return output

with open("out.txt", "rb") as inFile:
    lines = inFile.read()
    f = is_printable(lines)
    a = len(f)
    print(f)
    '''

'''
with open("out2.txt", "wb") as inFile:
    b = bytes([1,2,3,4])
    c = bytearray(b)
    for i in c:
        inFile.write(bytes(i))
    a = len(f)
    print(f)


with open("in.txt", "rb") as inFile:
    data = inFile.read()
    f = is_printable(data)
    print(len(f))
    b = f[-100:]
    c = 1


#given a block of bytes, returns true if it's all zeroes
def check_sparse(blk):
    for i in blk:
        if i != 0:
            return False
    return True
    '''
