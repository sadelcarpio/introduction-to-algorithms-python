class InsertionSort:

    @staticmethod
    def sort(a: list):
        for i in range(1, n):
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

    @staticmethod
    def binary_insert(a: list, key: int, p: int, r: int):
        q = int((p + r) / 2)
        if p >= r:
            return p
        if key == a[q]:
            return q
        if key < a[q]:
            return InsertionSort.binary_insert(a, key, p, q)
        return InsertionSort.binary_insert(a, key, q + 1, r)

    @staticmethod
    def sort_with_binary_search(a: list, n: int):
        for i in range(1, n):
            key = a[i]
            index = InsertionSort.binary_insert(a, key, 0, i)
            j = i - 1
            while j >= index:
                a[j + 1] = a[j]
                j = j - 1
            a[j + 1] = key


if __name__ == "__main__":
    arr = [5, 2, 4, 6, 1, 3]
    InsertionSort.sort_with_binary_search(a=arr, n=len(arr))
    print(arr)
