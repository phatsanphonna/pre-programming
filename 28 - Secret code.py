'''
Secret Code.py
'''


def main():
    '''This is main function.'''

    passcode = input()
    _i1, i2_value, _i3, i4_value, _i5, i6_value, _i7, i8_value, _i9, i10_value = list(
        passcode)

    print(i2_value + i4_value + i6_value + i8_value + i10_value)


main()
