#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    if not tuple_a or not tuple_b:
        print()
    len1 = len(tuple_a)
    len2 = len(tuple_b)
    if len1 == 0 and len2 == 0:
        print()
    elif len1 < 2:
        if len1 == 0:
            new_tuple = (0 + tuple_b[0], 0 + tuple_b[1])
        else:
            new_tuple = (tuple_a[0] + tuple_b[0], 0 + tuple_b[1])
    elif len2 < 2:
        if len2 == 0:
            new_tuple = (tuple_a[0] + 0, tuple_a[1] + 0)
        else:
            new_tuple = (tuple_a[0] + tuple_b[0], tuple_a[1] + 0)
    elif len1 >= 2 or len2 >= 2:
        new_tuple = (tuple_a[0] + tuple_b[0], tuple_a[1] + tuple_b[1])
    return (new_tuple)
