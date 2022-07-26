'''
สมการตัวน้อย.py
'''


def main():
    '''This is main function.'''

    a_variable = int(input())
    b_variable = int(input())
    c_variable = int(input())
    d_variable = int(input())
    x_variable = int(input())
    y_variable = int(input())

    equation = (
        (
            (b_variable / (a_variable * a_variable / d_variable))
            + (x_variable * b_variable / a_variable)
        ) * y_variable
    ) / (
        y_variable * c_variable
    )

    print('%.2f' % round(equation, 2))


main()
