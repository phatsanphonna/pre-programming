'''
เลือกคนคุยให้หน่อย.py
'''


GROUP_OF_PERSONS = {
    ('Calm', 'Empathetic'): 'Ice',
    ('Reliable', 'Courageous'): 'Fern',
    ('Optimistic', 'Cheerful'): 'Bam',
    ('Attractive', 'Creative'): 'Tangmo',
    ('Cheerful', 'Creative'): 'Mild',
    ('Reliable', 'Optimistic'): 'Prae',
    ('Calm', 'Courageous'): 'Dream',
    ('Empathetic', 'Attractive'): 'Aom'
}


def main():
    '''This is main function'''

    habit1 = input()
    habit2 = input()

    habits = [habit1, habit2]

    person = GROUP_OF_PERSONS.get(tuple(habits))

    if not person:
        person = GROUP_OF_PERSONS.get(tuple(habits[::-1]))

    print(person)


main()
