'''
Quiz 04
Cycle Locker
'''

ROTATION = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
REVERSED_ROTATION = ['9', '8', '7', '6', '5', '4', '3', '2', '1', '0']


def main():
    '''This is main function'''

    password = input()
    random_password = input()

    match_password = []

    tries = 0

    for i in range(4):
        match_password.append([password[i], random_password[i]])

    for password in match_password:
        password_index1 = ROTATION.index(password[0])
        password_index2 = ROTATION.index(password[1])

        reversed_password_index1 = REVERSED_ROTATION.index(password[0])
        reversed_password_index2 = REVERSED_ROTATION.index(password[1])

        password_index = password_index1 - password_index2
        reversed_password_index = reversed_password_index1 - reversed_password_index2

        print(password_index, reversed_password_index)

        if password_index <= reversed_password_index:
            tries += abs(password_index)
        else:
            tries += abs(10 + reversed_password_index)

    print(tries)


main()
