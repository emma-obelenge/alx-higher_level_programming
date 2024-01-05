#!/usr/bin/python3
for i in range(97, 97 + 26):
    if i == ord('q') or i == ord('e'):
        continue
    print(chr(i).format(), end='')
