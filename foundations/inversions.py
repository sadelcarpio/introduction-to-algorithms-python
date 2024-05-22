class NumInversions:

    @staticmethod
    def count_inversions(a: list, p: int, r: int):
        num_inversions = 0
        if p < r:
            q = int((p + r) / 2)
            num_inversions += NumInversions.count_inversions(a, p, q)
            num_inversions += NumInversions.count_inversions(a, q + 1, r)
            num_inversions += NumInversions.merge(a, p, q, r)
        # base case
        return num_inversions  # you need to return something, by default Python returns None

    @staticmethod
    def merge(a: list, p: int, q: int, r: int):
        num_inversions = 0
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
                num_inversions += (n_l - i)  # add the next elements of the left side since it's ordered!
            k = k + 1
        while i < n_l:
            a[k] = L[i]
            i = i + 1
            k = k + 1
        while j < n_r:
            a[k] = R[j]
            j = j + 1
            k = k + 1
        return num_inversions


if __name__ == '__main__':
    arr = [6, 5, 9, 0, 1, 7]
    num_inversions = NumInversions.count_inversions(a=arr, p=0, r=len(arr) - 1)
    print(num_inversions)
