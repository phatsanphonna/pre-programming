'''
เค้กช็อกโกแลต.py
'''


def main():
    '''This is main function'''

    money = int(input())
    price = int(input())

    total_cake, money_left = divmod(money, price)

    if not total_cake:
        print('Not enough money;(')
        print('Money left:', money_left)
        return

    print('Chocolate Cake:', total_cake)
    print('Money left:', money_left)


main()
