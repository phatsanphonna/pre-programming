'''
Simple matrix.py
'''


def main():
    '''This is main function'''

    rows = int(input())
    columns = int(input())

    for i in range(rows):
        for j in range(columns):
            if j + 1 == columns:
                print((i+1) * (j+1))
            else:
                print((i+1) * (j+1), end=' ')


main()
