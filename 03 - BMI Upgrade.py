'''
BMI Upgrade.py
'''


def convert_cm_to_m(centimeters: int):
    '''convert centimeters to meters'''

    return centimeters / 100


def find_bmi_value(weight: int, height: float):
    '''find BMI value'''

    return weight / (height**2)


def main():
    '''This is main function'''

    weight = float(input())
    height = float(input())
    age = int(input())

    if age <= 18:
        return print('Please use BMI for Children and Teens.')

    height = convert_cm_to_m(height)

    bmi = find_bmi_value(weight, height)

    if bmi < 16:
        print('Severe Thinness')
    elif bmi > 16 and bmi <= 16.99:
        print('Moderate Thinness')
    elif bmi >= 17 and bmi <= 18.49:
        print('Mild Thinness')
    elif bmi >= 18.5 and bmi <= 24.99:
        print('Normal')
    elif bmi >= 25 and bmi <= 29.99:
        print('Overweight')
    elif bmi >= 30 and bmi <= 34.99:
        print('Obese Class I')
    elif bmi >= 35 and bmi <= 39.99:
        print('Obese Class II')
    else:
        print('Obese Class III')


main()
