#!/usr/bin/env python3
import sys
from base64 import b64encode, b64decode
from zlib import crc32

linesize = 60

prologue = '''
import sys
from base64 import b64encode, b64decode
from zlib import crc32

linesize = 60

def binary():
    sys.stdout = sys.stdout.detach()
    for line in lines:
        start = line[0]
        b64 =  line[1]
        crc =  line[2]
        if crc32(b64.encode()) != crc :
            print('Aborting. Checksum (crc32) does not match\\n' + line, 
                  file = sys.stderr)
            sys.exit()
        lineout = b64decode(b64)
        sys.stdout.write(lineout)

lines = [
'''

epilogue = '''
]

binary()
'''

def printable():
    sys.stdin = sys.stdin.detach()
    enc = b64encode(sys.stdin.read())
    print(prologue)
    start = 0
    while start < len(enc):
        line = enc[start : start + linesize]
        crc = crc32(line)
        print('({}, "{}", {}),'.format(start, line.decode(), crc))
        start = start + linesize
    print(epilogue)

printable()
