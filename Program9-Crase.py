"""
Program: Project9
Author: Cole Crase
This program is to computes and prints the average of the numbers
in a text file while using two higer-order functions.
"""

def numberList(filename):
    with open(filename,'r') as f:
        read = f.read().split('\n')
        numberList = [int(num) for num in read]
    return numberList

def avg(filename, func):
    numbers = func(filename)
    return sum(numbers)/len(numbers)

def main():
    filename = input("Please enter the file name: ")
    average = avg(filename, numberList)
    print("The average is ", average)

main()
