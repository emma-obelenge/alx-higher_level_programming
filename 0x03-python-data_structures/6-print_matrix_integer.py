#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if not matrix:
        print()
    else:
        for i in matrix:
            for j in i:
                print(j, end='')
            print()
