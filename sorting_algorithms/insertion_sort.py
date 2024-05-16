class InsertionSort:

    @staticmethod
    def sort(a: list):
        for i in range(1, len(a)):
            key = a[i]
            j = i - 1
            while j >= 0 and a[j] > key:
                a[j + 1] = a[j]
                j = j - 1
            a[j + 1] = key
        return a


if __name__ == "__main__":
    arr = [5, 2, 4, 6, 1, 3]
    InsertionSort().sort(a=arr)
    print(arr)
