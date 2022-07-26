'''
คู่อันดับแบบตามใจฉัน.py
'''


def main():
    '''This is main function'''

    rows = int(input())
    columns = int(input())

    for i in range(1, rows+1):
        for j in range(1, columns+1):
            if j == columns:
                print('(%d, %d)' % (i, j))
            else:
                print('(%d, %d)' % (i, j), end=' ')


main()
