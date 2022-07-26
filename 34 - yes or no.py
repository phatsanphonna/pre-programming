'''
yes or no.py
'''


def main():
    '''This is main function'''

    sentence = input()

    if '.' in sentence:
        print("No, it's not.")
    elif ' ' in sentence:
        print("No, it's not.")
    elif "'" in sentence:
        print("No, it's not.")
    elif "~" in sentence:
        print("No, it's not.")
    else:
        print('Yes, it is.')


main()
