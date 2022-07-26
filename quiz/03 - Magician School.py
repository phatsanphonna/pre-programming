'''
Quiz 03
Magician School
'''


def main():
    '''This is main function'''

    grade = ''

    fullname = input()
    age = int(input())
    sex = input().lower()
    height = float(input())

    if age >= 13 and age <= 15:
        if sex == 'male':
            if height >= 160:
                grade = 'You can study in junior high school.'
            else:
                grade = 'You can not join this school.'
        elif sex == 'female':
            if height >= 155:
                grade = 'You can study in junior high school.'
            else:
                grade = 'You can not join this school.'
        else:
            grade = 'You can not join this school.'

    elif age >= 16 and age <= 18:
        if sex == 'male':
            if height >= 170:
                grade = 'You can study in senior high school.'
            else:
                grade = 'You can not join this school.'
        elif sex == 'female':
            if height >= 165:
                grade = 'You can study in senior high school.'
            else:
                grade = 'You can not join this school.'
        else:
            grade = 'You can not join this school.'
            
    else:
        grade = 'You can not join this school.'

    print(
        '%s %s Age: %d Height: %.2f' % (
            'Mr.' if sex == 'male' else 'Miss',
            fullname,
            age,
            height
        )
    )
    print(grade)


main()
