class BubbleSort:

    @staticmethod
    def sort(a: list, n: int):
        for i in range(n):
            for j in range(n - 1, i, -1):
                if a[j] < a[j - 1]:
                    a[j], a[j - 1] = a[j - 1], a[j]


if __name__ == '__main__':
    arr = [5, 2, 4, 6, 1, 3]
    BubbleSort.sort(a=arr, n=len(arr))
    print(arr)
