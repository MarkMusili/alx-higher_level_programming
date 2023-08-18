#!/usr/bin/python3
def best_score(a_dictionary):
    if not a_dictionary:
        return None

    res = max(a_dictionary.values())
    name = None

    for name, value in a_dictionary.items():
        if value == res:
            break
    return name
