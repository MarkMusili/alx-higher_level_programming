#!/usr/bin/python3
"""
This module adds all arguments to a python list,
then into a file
"""
import sys
save = __import__('5-save_to_json_file').save_to_json_file
load = __import__('6-load_from_json_file').load_from_json_file


def main():
    """
    Args:
        takes only command line argumenrs
    Return:
        (list) of arguments
    """
    args = sys.argv[1:]

    try:
        data = load("add_item.json")
    except Exception:
        data = []

    my_list = data + args

    save(my_list, "add_item.json")


if __name__ == "__main__":
    main()
