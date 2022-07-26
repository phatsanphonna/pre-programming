'''
Arithmetic Sequence.py
'''


def main():
    '''This is main function'''

    array = []

    a1_value = int(input())
    len_of_array = int(input())
    difference = int(input())

    for i in range(len_of_array):
        final_value = 0

        if i == 0:
            final_value += a1_value
        else:
            final_value += a1_value + difference * i

        array.append(final_value)

    print(*array, sep=' ', end='')


main()
