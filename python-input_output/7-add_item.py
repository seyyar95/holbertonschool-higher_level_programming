#!/usr/bin/python3
"""Module Doc"""


if __name__ == "__main__":

    import sys

    save_to_json_file = __import__('5-save_to_json_file').save_to_json_file

    load_from_json_file = __import__('6-load_from_json_file').\
        load_from_json_file

    n = len(sys.argv)
    my_list = []

    try:
        filename = "add_item.json"
        my_list = load_from_json_file(filename)
    except FileNotFoundError:
        pass
    finally:
        for i in range(1, n):
            my_list.append(sys.argv[i])
        save_to_json_file(my_list, "add_item.json")
