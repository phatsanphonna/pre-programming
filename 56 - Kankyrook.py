'''Kangyrook'''


def main():
    '''This is main function'''

    game_result = input().split()

    current_position = 0
    total_distance = 0

    for position in game_result:
        total_distance += abs(current_position - float(position))
        current_position = float(position)

    print('%.2f' % total_distance)


main()
