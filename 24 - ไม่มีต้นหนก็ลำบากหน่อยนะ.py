'''
ไม่มีต้นหนก็ลำบากหน่อยนะ.py
'''


def main():
    '''This is main function'''

    fishes = input().count('<^))))><')
    persons = int(input())

    if fishes == 0:
        print('No one will eat them  because we cannot be divided the fish.')
        return
        
    if fishes > persons:
        print('We have many fish ahoyy!!!')
        return

    if fishes == persons:
        print('We have enough fish for everyone.')
        return

    if persons % 2 == 1:
        print('No one will eat them  because we cannot be divided the fish.')
    else:
        print('We can share the fish together Yahoooo!!!')


main()
