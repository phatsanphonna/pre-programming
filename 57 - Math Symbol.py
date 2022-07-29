'''Math Symbol'''

OPERATOR_LIST = ['+', '-', '*', '/']


def calculate_by_operator(number_list: list, operator: str):
    '''Calculate every number in list by operator'''

    total = 0

    for index, number in enumerate(number_list):
        if index == 0:
            total = number
            continue

        if operator == '+':
            total += number
        elif operator == '-':
            total -= number
        elif operator == '*':
            total *= number
        elif operator == '/':
            total = number

    return total


def main():
    '''This is main function'''

    number_list = []
    operator = ''

    while True:
        number = input()

        if not number.isnumeric():
            if number in OPERATOR_LIST:
                operator = number
                break
            else:
                continue

        number_list.append(float(number))

    total = calculate_by_operator(number_list, operator)

    print('%.2f' % total)


main()
