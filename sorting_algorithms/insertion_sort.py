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

    @staticmethod
    def recursive_sort(a: list, n: int):
        if n == 1:
            return
        InsertionSort.recursive_sort(a, n - 1)
        key = a[n - 1]
        for i in range(n - 2, -1, -1):
            if key < a[i]:
                a[i + 1] = a[i]
                a[i] = key


if __name__ == "__main__":
    arr = [5, 2, 4, 6, 1, 3]
    InsertionSort().recursive_sort(a=arr, n=len(arr))
    print(arr)
