'''
Quiz 08
Snow White
'''


def main():
    '''This is main function'''

    members = []

    for _ in range(9):
        members.append(int(input()))

    members.sort()

    flag = False
    total = 0

    for member, i in enumerate(members):
        if total > 100:
            break

        if i == 6 and not total > 100:
            flag = True
            break
        
        total += member
        

    if flag:
        for i in range(0, len(members)-2):
            print(members[i])
    else:
        print('ERROR')

main()
