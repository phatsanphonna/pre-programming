'''
Basic Index
'''


def main():
    '''This is main function'''

    text_list = []

    while True:
        text = input()

        if text == 'END':
            break

        text_list.append(text)

    index = int(input())

    if text_list[index]:
        print('List[%d] = "%s"' % (index, text_list[index]))
    else:
        print('Index Not Found')


main()
