def uniq_add(my_list=[]):
    unique = list(set(my_list))
    sum = 0
    for value in unique:
        sum += value
    return (sum)