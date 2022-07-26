'''
Composite Function.py
'''


def function_f(value: float):
    '''return value of function f'''

    return (15 + value - (value**3)) / (((value**2) / 3) + 11)


def function_g(value: float):
    '''return value of function g'''

    return (value**3) + (4*value) - 1


def main():
    '''This is main function'''
    integer_number = float(input())
    function_type = input().lower()

    if function_type == 'gof':
        value = function_g(function_f(integer_number))

        print('%.2f' % round(value, 2))
    elif function_type == 'fog':
        value = function_f(function_g(integer_number))

        print('%.2f' % round(value, 2))


main()
