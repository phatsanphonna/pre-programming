'''
Walking average distance
'''


import math


def main():
    '''This is main function'''

    days = int(input())

    total_steps_list = []

    for _ in range(days):
        steps = int(input())
        total_steps_list.append(steps)

    average_steps = math.ceil(sum(total_steps_list) / days)

    for steps in total_steps_list:
        print(abs(average_steps - steps))


main()
