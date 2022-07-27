'''
4 Addict.py
'''

CALC_VALUE = float(input())
WORD_ = input()

TOTAL_VALUE = (
    (
        (
            ((CALC_VALUE + 4) ** 0.25) + (CALC_VALUE / 4)
        )
        / ((4*CALC_VALUE) - 4)
    ) * 44
)

REPEATED_VALUE = int(CALC_VALUE / 44)

print(WORD_ * REPEATED_VALUE)
print('%.4f' % round(TOTAL_VALUE, 4))
