'''
Quiz 10
Late Meeting
'''

from datetime import datetime, timedelta


def main():
    '''This is main function'''

    hours = int(input())
    minutes = int(input())
    seconds = int(input())
    relation = input()

    meeting_end_minutes = int(input())
    meeting_end_seconds = int(input())

    start_time_data = '%d:%d:%d %s' % (hours, minutes, seconds, relation)

    start_time = datetime.strptime(start_time_data, '%I:%M:%S %p')

    finish_time = start_time + \
        timedelta(minutes=meeting_end_minutes, seconds=meeting_end_seconds)

    print(
        datetime.strftime(
            finish_time, '%I:%M:%S %p'
        ).lower()
    )


main()
