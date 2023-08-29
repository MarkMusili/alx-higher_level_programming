#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    count = 0
    size = 0
    for element in my_list:
        size += 1
    try:
        for i in my_list:
            if count < x:
                print("{:d}".format(i), end="")
                count += 1
            elif count >= X:
                break
        if x > size:
            raise IndexError("IndexError: list index out of range")

    except (ValueError, TypeError):
            pass
    print()
    return count
