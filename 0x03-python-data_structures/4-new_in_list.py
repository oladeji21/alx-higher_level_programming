#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    if not my_list:
        return None
    if my_list == []:
        return None
    if my_list:
        new_list = my_list[:]
    if idx < 0 or idx > len(my_list)-1:
        return new_list
    else:
        new_list[idx] = element
        return new_list