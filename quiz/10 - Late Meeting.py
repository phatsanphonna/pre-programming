'''
Quiz 10
Late Meeting
'''


def main():
    '''This is main function'''

    hours = int(input())
    minutes = int(input())
    seconds = int(input())
    relation = input()

    meeting_end_minutes = int(input())
    meeting_end_seconds = int(input())

    converted_seconds = (hours * 60 * 60) + (minutes * 60) + seconds
    converted_meeting_ends_seconds = (
        meeting_end_minutes * 60) + meeting_end_seconds

    total_seconds = converted_seconds + converted_meeting_ends_seconds

    total_minutes, total_seconds = divmod(total_seconds, 60)
    total_hours, total_minutes = divmod(total_minutes, 60)

    if total_hours > 11:
        if relation == 'pm':
            relation = 'am'
        else:
            relation = 'pm'
    
    print('%.2d:%.2d:%.2d %s' % (
        total_hours, total_minutes, total_seconds, relation
    ))


main()
