'''
Quiz 01
Nintendo Battery
'''


def main():
    '''This is main function'''

    battery_left = int(input())
    gap = int(input())

    ratio = 100 / gap

    battery_left_ratio = int(battery_left // ratio)
    battery_used_ratio = gap - battery_left_ratio

    print('(' + ('O'*battery_left_ratio) +
          ('_'*battery_used_ratio) + ')', str(battery_left) + '%')


main()
