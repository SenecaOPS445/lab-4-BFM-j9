#!/usr/bin/env python3
# Author ID: jowusu9

def is_digits(sobj):
    # place code here - loop through each character in sobj 
    if isinstance(sobj, str) and sobj.isdigit():
        return True
    return False

if __name__ == '__main__':
    test_list = ['x3058','3058','8503x','8503']
    for item in test_list:
        if is_digits(item):
            print(item,'is an integer.')
        else:
            print(item,'is not an integer.')