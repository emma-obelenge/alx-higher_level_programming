#!/usr/bin/python3
for i in range(10):
    for j in range(1, 10):
        if i > 0:
            if i != 8 and (j + i) != 9):
                print(f"{i}{j + i}".format(), end=", ")
            else:
                break
        else:
            print(f"{i}{j}".format(), end=", ")
            continue
print("89".format())
