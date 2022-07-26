'''
How many.py
'''


def main():
    '''This is main function'''

    sentence = input().lower()
    word = input().lower()

    word_count = sentence.count(word)

    if word_count == 0:
        return print('No word and character.')

    if len(word) == 1:
        return print('Character :', word_count)

    print('Word :', word_count)


main()
