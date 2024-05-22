def binary_search(a: list, val: int, p: int, r: int):
    q = int((p + r) / 2)
    if p >= r:
        return None
    if val == a[q]:
        return q
    if val < a[q]:
        return binary_search(a, val, p, q)
    return binary_search(a, val, q + 1, r)


if __name__ == '__main__':
    arr = [6, 5, 7, 3, 2, 1]
    arr.sort()
    print(arr)
    index = binary_search(a=arr, val=4, p=0, r=6)
    print(index)
