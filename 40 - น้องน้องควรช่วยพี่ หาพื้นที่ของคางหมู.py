'''
น้องน้องควรช่วยพี่ หาพื้นที่ของคางหมู.py
'''


def find_trapezoidal_area(height: float, length: float):
    '''find area of trapezoidal'''

    return 1/2 * length * height


HEIGHT_ = float(input())
LENGTH1_ = float(input())
LENGTH2_ = float(input())

AREA_ = find_trapezoidal_area(HEIGHT_, LENGTH1_ + LENGTH2_)

print("Trapezoidal area = %.2f" % round(AREA_, 2))
