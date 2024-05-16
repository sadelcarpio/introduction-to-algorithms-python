class MergeSort:
    @staticmethod
    def sort(a: list, p: int, r: int):
        if p >= r:
            return
        q = int((p + r) / 2)
        MergeSort.sort(a, p, q)
        MergeSort.sort(a, q + 1, r)
        MergeSort.merge(a, p, q, r)

    @staticmethod
    def merge(a: list, p: int, q: int, r: int):
        n_l = q - p + 1
        n_r = r - q
        L = a[p:p + n_l]
        R = a[p + n_l:p + n_l + n_r]
        i, j, k = 0, 0, p
        while i < n_l and j < n_r:
            if L[i] <= R[j]:
                a[k] = L[i]
                i = i + 1
            else:
                a[k] = R[j]
                j = j + 1
            k = k + 1
        while i < n_l:
            a[k] = L[i]
            i = i + 1
            k = k + 1
        while j < n_r:
            a[k] = R[j]
            j = j + 1
            k = k + 1


if __name__ == '__main__':
    arr = [12, 3, 7, 9, 14, 6, 11, 2]
    MergeSort().sort(a=arr, p=0, r=7)
    print(arr)
