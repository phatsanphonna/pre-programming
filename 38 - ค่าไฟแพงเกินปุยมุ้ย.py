'''
ค่าไฟแพงเกินปุยมุ้ย!!.py
'''


def calculate_unit(watt: int, hours: float):
    '''Calculate unit'''

    return (watt * hours) / 1000


def main():
    '''This is main function'''
    
    a_watt = int(input())
    b_watt = int(input())
    c_watt = int(input())
    d_watt = int(input())
    e_watt = int(input())

    a_unit = calculate_unit(a_watt, 3)
    b_unit = calculate_unit(b_watt, 1)
    c_unit = calculate_unit(c_watt, 0.5)
    d_unit = calculate_unit(d_watt, 5)
    e_unit = calculate_unit(e_watt, 24)

    print('TV %d Watt 1 ea for 3 hours' % a_watt)
    print('%.2f unit.' % a_unit)
    print('Microwave %d Watt 1 ea for 1 hours' % b_watt)
    print('%.2f unit.' % b_unit)
    print('Hair dryer %d Watt 1 ea for 0.5 hours' % c_watt)
    print('%.2f unit.' % c_unit)
    print('light bulb %d Watt 4 ea for 5 hours' % d_watt)
    print('%.2f unit.' % d_unit)
    print('Refrigerator %d Watt 1 ea for 24 hours' % e_watt)
    print('%.2f unit.' % e_unit)


main()
