'''
ตารางสูตรคูณแบบตามใจฉัน.py
'''


def main():
    '''This is main function'''

    n_value = int(input())
    m_value = int(input())

    print('-----')

    for i in range(2, n_value+1):
        for j in range(m_value):
            print(str(i) + ' x ' + str(j+1) + ' = ' + str(i*(j+1)))

        print('-----')


main()
