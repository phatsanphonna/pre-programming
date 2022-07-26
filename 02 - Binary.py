'''
Binary.py
'''


def main():
    '''This is main function'''

    number = input()
    number_binary = bin(int(number)).split('b')[1]

    number_binary = number_binary.replace('1', 'open ')
    number_binary = number_binary.replace('0', 'close ')

    number_binary = number_binary.split(' ')[:-1]

    print(*number_binary, sep=', ', end='')


main()
