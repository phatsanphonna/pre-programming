'''
Choose a book.py
'''

from math import factorial


def main():
    '''This is main function'''

    n_value = int(input())
    r_value = int(input())

    chooses = factorial(n_value) // (
        factorial(r_value) * (factorial(n_value - r_value))
    )

    print(chooses)


main()
