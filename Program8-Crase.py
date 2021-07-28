"""
Program: Project8
Author: Cole Crase
This program is to check if Lee's function definition is working as expected.
"""

def printAll(seq):
    if seq:
        print(seq[0])
        printAll(seq[1:])
printAll("What's up world!") #TheString
printAll((1,2,3,4,)) #TheTuple
printAll([1,2,3,4]) #TheList
