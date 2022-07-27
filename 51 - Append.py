'''
Append.py
'''


def main():
    '''This is main function'''

    array = []
    array_length = int(input())

    for _ in range(array_length):
        word = input()
        array.append(word)

    array_str = str(array.copy()).replace("'", '"')

    print(array_str)


main()
