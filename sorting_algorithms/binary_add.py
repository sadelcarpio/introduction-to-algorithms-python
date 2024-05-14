class BinaryAdd:

    @staticmethod
    def add_binary_integers(a: list, b: list, n: int):
        c = [0] * (n + 1)
        carry = 0
        for i in range(n - 1, -1, -1):
            suma = a[i] + b[i] + carry
            c[i + 1] = suma % 2
            c[i] = carry
            carry = suma // 2
        return c


if __name__ == '__main__':
    c = BinaryAdd.add_binary_integers([1, 1, 0, 1], [1, 0, 1, 1], 4)
    print(c)
