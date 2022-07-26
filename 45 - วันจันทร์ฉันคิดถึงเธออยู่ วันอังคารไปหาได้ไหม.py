'''
วันจันทร์ฉันคิดถึงเธออยู่ วันอังคารไปหาได้ไหม.py
'''


def main():
    '''This is main function'''

    time = int(input())

    minutes, seconds = divmod(time, 60)
    hours, minutes = divmod(minutes, 60)
    days, hours = divmod(hours, 24)

    print('%.2d:' % days + '%.2d:' % hours + '%.2d:' %
          minutes + '%.2d' % seconds)


main()
