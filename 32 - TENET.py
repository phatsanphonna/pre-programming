'''
TENET.py
'''


def is_parlindrome(string: str):
    '''Check if string is parlindrome'''

    return string == string[::-1]


def main():
    '''This is main function'''

    words = []

    loops = int(input())

    for _ in range(loops):
        words.append(input())

    for word in words:
        if is_parlindrome(word):
            print(word)


main()
