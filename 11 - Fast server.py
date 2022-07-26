'''
Fast server.py
'''


def convert_unit_to_seconds(time: int, unit: str):
    '''Convert unit'''

    if unit == 'Millisecond':
        return time * 0.001
    elif unit == 'Nanosecond':
        return time * 0.000000001
    elif unit == 'Picosecond':
        return time * 0.000000000001
    elif unit == 'Microsecond':
        return time * 0.000001


def main():
    '''This is main function'''

    server1_time = int(input())
    server1_unit = input()

    server2_time = int(input())
    server2_unit = input()

    converted_server1_time = convert_unit_to_seconds(
        server1_time, server1_unit)
    converted_server2_time = convert_unit_to_seconds(
        server2_time, server2_unit)

    if converted_server1_time > converted_server2_time:
        print('Server B,', '%.6f' % round(converted_server2_time, 6), 'second')
        print('Faster than server A ,', str(
            int(converted_server1_time // converted_server2_time)), 'times')
    elif converted_server1_time < converted_server2_time:
        print('Server A,', '%.6f' % round(converted_server1_time, 6), 'second')
        print('Faster than server B ,', str(
            int(converted_server2_time // converted_server1_time)), 'times')
    else:
        print('equal')


main()
