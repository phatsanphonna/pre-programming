'''
บวกเลขง่ายๆ.py
'''


def main():
    '''This is main function'''

    final_value = 0

    for _ in range(10):
        number = int(input())

        if number < 0:
            final_value += -5

        final_value += number

    if final_value < 0:
        print(-5)
        return

    print(final_value)


main()
