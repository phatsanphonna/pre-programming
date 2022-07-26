'''
สร้างกล่องข้อความ.py
'''


def make_box(times_loop: int, counter=1):
    '''Generate box'''

    if counter > times_loop:
        return

    print('-------------------------')
    print('|                       |')
    print('|                       |')
    print('|                       |')
    print('|   Pre-Progamming 65   |')
    print('|                       |')
    print('|                       |')
    print('|                       |')

    if counter == times_loop:
        print('-------------------------')

    counter += 1

    make_box(times_loop, counter)


def main():
    '''This is main function'''

    times_loop = int(input())

    make_box(times_loop)


main()
