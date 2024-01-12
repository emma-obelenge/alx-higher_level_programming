#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    dup_matrix = [row[:] for row in matrix]
    squared_matrix = [[item ** 2 for item in row] for row in dup_matrix]
    return (squared_matrix)
