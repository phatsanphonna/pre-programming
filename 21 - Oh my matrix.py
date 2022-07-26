'''
Oh! my matrix.py
'''


def find_det(matrix1: int, matrix2: int, matrix3: int, matrix4: int):
    '''find det value of matrix'''

    return (matrix1 * matrix4) - (matrix2 * matrix3)


MATRIX_A1 = int(input())
MATRIX_A2 = int(input())
MATRIX_A3 = int(input())
MATRIX_A4 = int(input())

MATRIX_C1 = int(input())
MATRIX_C2 = int(input())
MATRIX_C3 = int(input())
MATRIX_C4 = int(input())

MATRIX_B1 = MATRIX_C1 - MATRIX_A1
MATRIX_B2 = MATRIX_C2 - MATRIX_A2
MATRIX_B3 = MATRIX_C3 - MATRIX_A3
MATRIX_B4 = MATRIX_C4 - MATRIX_A4

D_VALUE = float(
    find_det(MATRIX_A1, MATRIX_A2, MATRIX_A3, MATRIX_A4)
    + find_det(MATRIX_B1, MATRIX_B2, MATRIX_B3, MATRIX_B4)
    + find_det(MATRIX_C1, MATRIX_C2, MATRIX_C3, MATRIX_C4)
)

print("b1: " + str(MATRIX_B1))
print("b2: " + str(MATRIX_B2))
print("b3: " + str(MATRIX_B3))
print("b4: " + str(MATRIX_B4))
print("D: " + "%.2f" % round(D_VALUE, 2))
