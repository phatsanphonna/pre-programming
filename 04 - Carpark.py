'''
Carpark.py
'''

HOURS_ORDER = (
    0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12,
    13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23
)


def calculate_hours_from_days(day_park: int, day_left: int):
    '''Calculate days to hours'''

    total_days = day_left - day_park

    if total_days < 0:
        return 'error'

    return total_days * 24


def main():
    '''This is main function'''

    total_hours = 0
    total_days = 0

    total_price = 0

    day_park = float(input())
    hour_park = float(input())

    day_left = float(input())
    hour_left = float(input())

    calc_hours = calculate_hours_from_days(day_park, day_left)

    if calc_hours == 'error':
        print('error')
        return

    total_hours = calc_hours

    hour_park_index = HOURS_ORDER.index(hour_park)
    hour_left_index = HOURS_ORDER.index(hour_left)

    if hour_park_index > hour_left_index:
        total_hours += len(HOURS_ORDER) - hour_park_index + hour_left_index
        total_hours -= 24
    else:
        total_hours += hour_left - hour_park

    if total_hours < 2:
        print('%d day %d hour' % (total_days, total_hours))
        print('%d baht' % total_price)

        return

    if total_hours > 2 and total_hours <= 12:
        total_price += total_hours * 15

        print('%d day %d hour' % (total_days, total_hours))
        print('%d baht' % total_price)

        return

    div_total_days, div_total_hours = divmod(total_hours, 24)
    div_total_weeks, div_total_days = divmod(div_total_days, 7)

    # Calculate price
    total_price += div_total_weeks * 1400
    total_price += div_total_days * 200

    # Calculate discount
    total_price += -(div_total_weeks * 300)

    if div_total_hours > 12:
        total_price += 200
    else:
        total_price += div_total_hours * 15

    if div_total_weeks >= 4:
        total_price -= 500

    print('%d day %d hour' %
          (div_total_days + (div_total_weeks * 7), div_total_hours))
    print('%d baht' % total_price)


main()
