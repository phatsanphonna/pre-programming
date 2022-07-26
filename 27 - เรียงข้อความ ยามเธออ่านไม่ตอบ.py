'''
เรียงข้อความ ยามเธออ่านไม่ตอบ.py
'''


def main():
    '''this is main function'''

    text1 = input().capitalize()
    text2 = input().capitalize()
    text3 = input().capitalize()

    arr = [text1, text2, text3]
    sorted_arr = sorted(arr, key=len)

    print(*sorted_arr, sep='\n', end='')


main()
