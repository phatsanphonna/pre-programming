'''
รหัสเป็นเช่นไร มองไปไหนเห็นแต่เธอ.py
'''

for i in range(5):
    passcode = input()

    print(('0'*(10 - len(passcode))) + passcode)
