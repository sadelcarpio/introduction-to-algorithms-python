class SelectionSort:

    @staticmethod
    def sort(A: list):
        n = len(A)
        for i in range(n - 1):
            minimum = A[i]
            index = i
            for j in range(i + 1, n):
                if A[j] < minimum:
                    minimum = A[j]
                    index = j
            A[index] = A[i]
            A[i] = minimum
        return A


if __name__ == "__main__":
    arr = SelectionSort().sort(A=[5, 2, 4, 6, 1, 3])
    print(arr)
