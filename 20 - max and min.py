'''
mx and mn.py
'''


def find_mx(num1: int, num2: int, num3: int, num4: int, num5: int):
    '''Find mximum value of five value'''

    final_value = num1

    if not final_value > num1:
        final_value = num1
    if not final_value > num2:
        final_value = num3
    if not final_value > num3:
        final_value = num3
    if not final_value > num4:
        final_value = num4
    if not final_value > num5:
        final_value = num5

    return final_value


def find_mn(num1: int, num2: int, num3: int, num4: int, num5: int):
    '''Find mnimum value of five value'''

    final_value = num1

    if not final_value < num1:
        final_value = num1
    if not final_value < num2:
        final_value = num3
    if not final_value < num3:
        final_value = num3
    if not final_value < num4:
        final_value = num4
    if not final_value < num5:
        final_value = num5

    return final_value


def main():
    '''This is main function'''

    mn_or_mx = input()

    num1 = int(input())
    num2 = int(input())
    num3 = int(input())
    num4 = int(input())
    num5 = int(input())

    if mn_or_mx == 'MIN':
        final_value = find_mn(num1, num2, num3, num4, num5)
        print('MIN :', final_value)
    elif mn_or_mx == 'MAX':
        final_value = find_mx(num1, num2, num3, num4, num5)
        print('MAX :', final_value)


main()
