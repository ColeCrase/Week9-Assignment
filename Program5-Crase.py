"""
Program: Project5
Author: Cole Crase
This program...
"""
theList = {"1", "2", "3", "4"}

def isSorted(lst):
    if len(lst) >= 0 and len(lst) < 2:
        return True
    else:
        for i in range(len(lst)-1):
            if lst[i] > lst [i + 1]:
                return False

