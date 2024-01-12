#!/usr/bin/python3
def search_replace(my_list, search, replace):
    dup_list = my_list.copy()
    for item in dup_list:
        if item == search:
            index = dup_list.index(item)
            dup_list[index] = replace
    return (dup_list)
