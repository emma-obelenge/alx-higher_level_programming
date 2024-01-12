#!/usr/bin/python3
def only_diff_elements(set_1, set_2):
    in_both = set_1.intersection(set_2)
    combined = set_1.union(set_2)
    return (combined.difference(in_both))
