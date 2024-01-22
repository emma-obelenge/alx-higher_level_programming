#!/usr/bin/python3

def safe_print_list_integers(my_list=[], x=0):
    count = 0
    for i in range(x):
        try:
            int_value = int(my_list[i])
            print("{:d}".format(my_list[i]), end='')
        except (ValueError, TypeError):
            pass
#        except IndexError as e:
#            print(e)
        else:
            count += 1
    print()
    return (count)
