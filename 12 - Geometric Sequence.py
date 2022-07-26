'''
Geometric Sequence.py
'''


def main():
    '''This is main function'''

    array = []

    a1_value = float(input())
    len_of_array = int(input())
    difference = float(input())

    for i in range(len_of_array):
        final_value = 0

        final_value += a1_value * (difference**i)

        array.append(final_value)

    for number in array:
        if array.index(number) == len_of_array:
            print('%.2f' % number, end='')
        else:
            print('%.2f' % number, end=' ')


main()
