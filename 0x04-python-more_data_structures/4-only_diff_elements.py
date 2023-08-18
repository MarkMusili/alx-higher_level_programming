#!/usr/bin/python3
def only_diff_elements(set_1, set_2):
    i = [i for i in set_1 if i not in set_2]
    n = [n for n in set_2 if n not in set_1]
    not_common = [i + n]
    return not_common
