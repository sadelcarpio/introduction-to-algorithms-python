from binary_search import binary_search
from merge_sort import MergeSort


class TwoSum:

    @staticmethod
    def search(a: list, n: int, x: int):
        MergeSort.sort(a, 0, n - 1)
        for i in range(0, n - 1):
            index = binary_search(a, x - a[i], i + 1, n)
            if index is not None:
                return True
        return False


if __name__ == '__main__':
    n = 6
    a = [6, 5, 8, 0, 1, 3]
    x = 10
    print(TwoSum.search(a, n, x))
