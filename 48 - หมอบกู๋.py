'''
หมอบกู๋.py
'''


def main():
    '''This is main function'''

    money = float(input())
    total_prices = []

    got_store = False

    for store in range(1, 11):
        if got_store:
            '''Don't do the action below if got a store to buy'''
            break

        total_prices.append([])

        for _ in range(1, 6):
            price_gotten = float(input())

            total_prices[store-1].append(price_gotten)

            if money > price_gotten:
                '''If ok with the deal'''

                print('%.2f' % round(price_gotten, 2))
                print(store)

                got_store = True
                break

    if got_store:
        '''Don't do the action below if got a store to buy'''
        return

    minimum_price = 0
    minimum_store = 0

    for prices in total_prices:
        '''Check the minimum price of each store'''

        min_price = min(prices)
        index = total_prices.index(prices)

        if minimum_price == 0:
            '''If this is first loop'''

            minimum_price = min_price
            minimum_store = index + 1

        if min_price < minimum_price:
            '''If min_price of this store lower than minimum_price'''

            minimum_price = min_price
            minimum_store = index + 1

    print('%.2f' % round(minimum_price, 2))
    print(minimum_store)


main()
