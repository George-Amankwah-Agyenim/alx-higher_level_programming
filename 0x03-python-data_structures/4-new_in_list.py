#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    my_list_duplicate = my_list.copy()
    if idx < 0 or idx >= len(my_list):
        pass
    else:
        my_list_duplicate[idx] = element
    return my_list_duplicate
