class MatMul:
    @staticmethod
    def naive_multiply(a: list[list], b: list[list], n: int) -> list[list]:
        c = [n * [0] for _ in range(n)]
        for i in range(n):
            for j in range(n):
                for k in range(n):
                    c[i][j] = c[i][j] + a[i][k] * b[k][j]
        return c

    @staticmethod
    def recursive_multiply(a: list[list], b: list[list]) -> list[list]:
        n = len(a)
        c = [n * [0] for _ in range(n)]
        MatMul._recursive_multiply(a, b, c, 0, 0, 0, 0, n)
        return c

    @staticmethod
    def _recursive_multiply(a: list[list], b: list[list], c: list[list], a_col: int, a_row: int, b_col: int, b_row: int,
                            n: int):
        if n == 1:
            c[a_row][b_col] += a[a_row][a_col] * b[b_row][b_col]
            return
        new_n = n // 2
        MatMul._recursive_multiply(a, b, c, a_col, a_row, b_col, b_row, new_n)
        MatMul._recursive_multiply(a, b, c, a_col + new_n, a_row, b_col, b_row + new_n, new_n)
        MatMul._recursive_multiply(a, b, c, a_col, a_row, b_col + new_n, b_row, new_n)
        MatMul._recursive_multiply(a, b, c, a_col + new_n, a_row, b_col + new_n, b_row + new_n, new_n)
        MatMul._recursive_multiply(a, b, c, a_col, a_row + new_n, b_col, b_row, new_n)
        MatMul._recursive_multiply(a, b, c, a_col + new_n, a_row + new_n, b_col, b_row + new_n, new_n)
        MatMul._recursive_multiply(a, b, c, a_col, a_row + new_n, b_col + new_n, b_row, new_n)
        MatMul._recursive_multiply(a, b, c, a_col + new_n, a_row + new_n, b_col + new_n, b_row + new_n, new_n)

    @staticmethod
    def strassen_multiply(a: list[list], b: list[list]) -> list[list]:
        n = len(a)
        return MatMul._strassen_multiply(a, b, 0, 0, 0, 0, n)

    @staticmethod
    def _strassen_multiply(a: list[list], b: list[list], a_col: int, a_row: int, b_col: int, b_row: int, n: int):
        c = [n * [0] for _ in range(n)]
        if n == 1:
            return [[a[a_row][a_col] * b[b_row][b_col]]]
        new_n = n // 2
        s = [(5 * new_n) * [0] for _ in range(2 * new_n)]
        p = [[new_n * [0] for _ in range(new_n)] for _ in range(7)]
        MatMul.matrix_sum(b, b, s, b_col + new_n, b_row, b_col + new_n, b_row + new_n, 0, 0, new_n, True)  # b12 - b22
        MatMul.matrix_sum(a, a, s, a_col, a_row, a_col + new_n, a_row, new_n, 0, new_n, False)  # a11 + a12
        MatMul.matrix_sum(a, a, s, a_col, a_row + new_n, a_col + new_n, a_row + new_n, 2 * new_n, 0, new_n,
                          False)  # a21 + a22
        MatMul.matrix_sum(b, b, s, b_col, b_row + new_n, b_col, b_row, 3 * new_n, 0, new_n, True)  # b21 - b11
        MatMul.matrix_sum(a, a, s, a_col, a_row, a_col + new_n, a_row + new_n, 4 * new_n, 0, new_n, False)  # a11 + a22
        MatMul.matrix_sum(b, b, s, b_col, b_row, b_col + new_n, b_row + new_n, 0, new_n, new_n, False)  # b11 + b22
        MatMul.matrix_sum(a, a, s, a_col + new_n, a_row, a_col + new_n, a_row + new_n, new_n, new_n, new_n,
                          True)  # a12 - a22
        MatMul.matrix_sum(b, b, s, b_col, b_row + new_n, b_col + new_n, b_row + new_n, 2 * new_n, new_n, new_n,
                          False)  # b21 + b22
        MatMul.matrix_sum(a, a, s, a_col, a_row, a_col, a_row + new_n, 3 * new_n, new_n, new_n, True)  # a11 - a21
        MatMul.matrix_sum(b, b, s, b_col, b_row, b_col + new_n, b_row, 4 * new_n, new_n, new_n, False)  # b11 + b12

        p[0] = MatMul._strassen_multiply(a, s, a_col, a_row, 0, 0, new_n)
        p[1] = MatMul._strassen_multiply(s, b, new_n, 0, b_col + new_n, b_row + new_n, new_n)
        p[2] = MatMul._strassen_multiply(s, b, 2 * new_n, 0, b_col, b_row, new_n)
        p[3] = MatMul._strassen_multiply(a, s, a_col + new_n, a_row + new_n, 3 * new_n, 0, new_n)
        p[4] = MatMul._strassen_multiply(s, s, 4 * new_n, 0, 0, new_n, new_n)
        p[5] = MatMul._strassen_multiply(s, s, new_n, new_n, 2 * new_n, new_n, new_n)
        p[6] = MatMul._strassen_multiply(s, s, 3 * new_n, new_n, 4 * new_n, new_n, new_n)

        MatMul.c11(p, c, 0, 0, new_n)
        MatMul.c12(p, c, new_n, 0, new_n)
        MatMul.c21(p, c, 0, new_n, new_n)
        MatMul.c22(p, c, new_n, new_n, new_n)
        return c

    @staticmethod
    def c11(p: list, c: list[list], c_col: int, c_row: int, n: int):
        for i in range(n):
            for j in range(n):
                c[c_row + i][c_col + j] += p[4][i][j] + p[3][i][j] - p[1][i][j] + p[5][i][j]

    @staticmethod
    def c12(p: list, c: list[list], c_col: int, c_row: int, n: int):
        for i in range(n):
            for j in range(n):
                c[c_row + i][c_col + j] += p[0][i][j] + p[1][i][j]

    @staticmethod
    def c21(p: list, c: list[list], c_col: int, c_row: int, n: int):
        for i in range(n):
            for j in range(n):
                c[c_row + i][c_col + j] += p[2][i][j] + p[3][i][j]

    @staticmethod
    def c22(p: list, c: list[list], c_col: int, c_row: int, n: int):
        for i in range(n):
            for j in range(n):
                c[c_row + i][c_col + j] += p[4][i][j] + p[0][i][j] - p[2][i][j] - p[6][i][j]

    @staticmethod
    def matrix_sum(a: list[list], b: list[list], s: list[list], a_col: int, a_row: int, b_col: int, b_row: int,
                   s_col: int, s_row: int, n: int, neg: bool = False):
        for i in range(n):
            for j in range(n):
                s[s_row + i][s_col + j] = a[i + a_row][j + a_col] + (b[i + b_row][j + b_col] if not neg else (-b[i + b_row][j + b_col]))


if __name__ == '__main__':
    a = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]]
    b = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]]
    c = MatMul.strassen_multiply(a, b)
    print(c)
