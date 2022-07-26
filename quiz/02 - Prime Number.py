'''
Quiz 02
Prime Number
'''


def main():
    '''This is main function'''

    flag = False

    number = int(input())

    if number == 0:
        print('Not Prime Number')
        return
        
    if number > 1:
        for i in range(2, number):
            if number % i == 0:
                flag = True
                break

    if flag:
        print('Not Prime Number')
    else:
        print('Prime Number')


main()
