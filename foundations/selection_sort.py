class SelectionSort:

    @staticmethod
    def sort(a: list):
        n = len(a)
        for i in range(n - 1):
            minimum = a[i]
            index = i
            for j in range(i + 1, n):
                if a[j] < minimum:
                    minimum = a[j]
                    index = j
            a[index] = a[i]
            a[i] = minimum


if __name__ == "__main__":
    arr = [5, 2, 4, 6, 1, 3]
    SelectionSort.sort(a=arr)
    print(arr)
