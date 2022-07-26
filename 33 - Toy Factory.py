'''
Toy Factory.py
'''


def generate_part(part: int):
    '''Generate part of toy body'''

    if part == 1:
        print(' ^----^')
    elif part == 2:
        print('( 0--0 )')
    elif part == 3:
        print('<------>')
    elif part == 4:
        print('(------)')
    elif part == 5:
        print(' u----u')


def main():
    '''This is main function'''

    part_1 = int(input())
    part_2 = int(input())
    part_3 = int(input())
    part_4 = int(input())
    part_5 = int(input())

    generate_part(part_1)
    generate_part(part_2)
    generate_part(part_3)
    generate_part(part_4)
    generate_part(part_5)


main()
