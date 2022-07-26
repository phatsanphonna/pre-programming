'''
Quiz 05
Pager
'''


def main():
    '''This is main function'''

    text = input()

    text_length = len(text)

    alphabets_20, alphabets_left = divmod(text_length, 20)
    alphabets_8, alphabets_left = divmod(alphabets_left, 8)
    alphabets_3, alphabets_left = divmod(alphabets_left, 3)
    alphabets_1, alphabets_left = divmod(alphabets_left, 1)

    price = 0

    price += alphabets_20 * 18.5
    price += alphabets_8 * 6.5
    price += alphabets_3 * 3
    price += alphabets_1 * 1.5

    print("Text's length is : " + '"%d"' % text_length)
    print('Total price is   : %.2f Baht\.-' % price)


main()
