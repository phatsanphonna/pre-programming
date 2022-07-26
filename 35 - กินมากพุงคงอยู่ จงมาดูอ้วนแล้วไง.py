'''
กินมากพุงคงอยู่ จงมาดูอ้วนแล้วไง.py
'''


def convert_cm_to_m(centimeters: int):
    '''convert centimeters to meters'''

    return centimeters / 100


def find_bmi_value(weight: int, height: float):
    '''find BMI value'''

    return weight / (height**2)


NAME_ = input()
WEIGHT_ = int(input())
HEIGHT_ = int(input())

HEIGHT_ = convert_cm_to_m(HEIGHT_)

BMI_ = find_bmi_value(WEIGHT_, HEIGHT_)

print('Name:', NAME_)
print('Weight:', WEIGHT_, 'kg.')
print('Height: ' + '%.2f' % round(HEIGHT_, 2) + ' m.')
print('BMI: %.2f' % round(BMI_, 2))
