class InsertionSort:

    @staticmethod
    def sort(A: list):
        for i in range(1, len(A)):
            key = A[i]
            j = i - 1
            while j >= 0 and A[j] > key:
                A[j + 1] = A[j]
                j = j - 1
            A[j + 1] = key
        return A


if __name__ == "__main__":
    arr = InsertionSort().sort(A=[5, 2, 4, 6, 1, 3])
    print(arr)
