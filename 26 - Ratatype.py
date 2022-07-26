'''
Ratatype.py
'''


def main():
    '''This is main function'''

    sentence = input().upper()

    clicks = 0

    for character in sentence:
        if character == '6':
            clicks += 1
        elif character == 'Y':
            clicks += 1
        elif character == 'H':
            clicks += 1
        elif character == 'N':
            clicks += 1
        elif character == '7':
            clicks += 1
        elif character == 'U':
            clicks += 1
        elif character == 'J':
            clicks += 1
        elif character == 'M':
            clicks += 1

    print(clicks)


main()
