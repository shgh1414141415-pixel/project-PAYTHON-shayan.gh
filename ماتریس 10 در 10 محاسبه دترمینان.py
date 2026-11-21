import random

def determinant(matrix):
    n = len(matrix)

    m = []
    for row in matrix:
        m.append(row[:])

    det = 1

    for i in range(n):
        max_row = i
        for k in range(i + 1, n):
            if abs(m[k][i]) > abs(m[max_row][i]):
                max_row = k

        if m[max_row][i] == 0:
            return 0

        if max_row != i:
            m[i], m[max_row] = m[max_row], m[i]
            det = -det

        det = det * m[i][i]

        for k in range(i + 1, n):
            factor = m[k][i] / m[i][i]
            for j in range(i, n):
                m[k][j] = m[k][j] - factor * m[i][j]

    if abs(det - round(det)) < 1e-9:
        det = round(det)

    return det


def make_random_matrix(size):
    matrix = []
    for i in range(size):
        row = []
        for j in range(size):
            row.append(random.randint(1, 9))
        matrix.append(row)
    return matrix


for test in range(5):
    print("=" * 50)
    print("Matrix number", test + 1)
    print("=" * 50)

    matrix = make_random_matrix(10)

    for row in matrix:
        print(row)

    result = determinant(matrix)
    print("\nDeterminant =", result)
    print()