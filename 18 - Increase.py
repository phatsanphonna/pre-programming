'''
Increase.py
'''


def main():
    '''This is main function'''

    final_value = 0

    while True:
        value = int(input())

        if value < 0:
            break

        final_value += value

    print(final_value)


main()
