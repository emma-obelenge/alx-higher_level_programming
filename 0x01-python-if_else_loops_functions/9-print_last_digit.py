#/usr/bin/python3
def print_last_digit(number):
    if number < 0:
        digit = number % -10
        print(f"{digit}", end='')
    elif number == 0:
        digit = number
        print(f"{digit}", end='')
    else:
        digit = number % 10
        print(f"{digit}", end='')
    return(digit)
print_last_digit = __import__('9-print_last_digit').print_last_digit

print_last_digit(98)
print_last_digit(0)
r = print_last_digit(-1024)
print(r)