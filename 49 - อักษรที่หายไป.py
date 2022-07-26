'''
อักษรที่หายไป.py
'''


def main():
    '''This is main function.'''

    sentence = input().split('"')

    if len(sentence) == 1:
        return print('No error')

    sentence[1] = chr(int(sentence[1]))

    print(*sentence, sep='')


main()
