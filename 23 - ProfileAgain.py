'''
ProfileAgain.py
'''


def set_prefix(prefix: str):
    '''Get prefix of sex'''

    name_prefix = {
        'female': 'Mrs.',
        'male': 'Mr.'
    }

    return name_prefix[prefix]


def main():
    '''This is main function'''

    sex = input().lower()
    id_ = input()
    firstname = input().capitalize()
    lastname = input().capitalize()
    age = input()
    occupation = input().upper()

    sex_prefix = set_prefix(sex.lower())

    print('======')
    print('ID :', id_[0:6])
    print('Name :', sex_prefix, firstname, lastname)
    print('Age :', age, 'years old')
    print('Occupation :', occupation)
    print('======')


main()
