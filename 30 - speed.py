'''
speed.py
'''


def convert_nm_to_meters(nautical_miles: float):
    '''convert nautical miles to meters'''

    return nautical_miles * 1852


def convert_ms_to_s(milliseconds: int):
    '''convert milliseconds to seconds'''

    return milliseconds / 1000


DISTANCE_NM = float(input())
TIME_MS = int(input())


DISTANCE_METERS = convert_nm_to_meters(DISTANCE_NM)
TIME_S = convert_ms_to_s(TIME_MS)

VELOCITY_ = DISTANCE_METERS / TIME_MS

print("อัตราเร็วเท่ากับ : %.3f เมตรต่อวินาที" % round(VELOCITY_ * 1000, 3))
