from util import swap


def _quickSort(arr, i, j):
    if j - i <= 1:
        return arr

    pivot = arr[j - 1]
    l, r = i, j - 2
    while True:
        while l <= r and arr[l] <= pivot:
            l += 1
        while l <= r and arr[r] >= pivot:
            r -= 1
        if l <= r:
            swap(arr, l, r)
        else:
            break
    swap(arr, l, j - 1)
    _quickSort(arr, i, l)
    _quickSort(arr, l + 1, j)
    return arr


def quickSort(arr):
    return _quickSort(arr, 0, len(arr))


if __name__ == '__main__':
    arr = [2, 3, 4, 2, 0, 1, 3, 2, 4]
    print(quickSort(arr))
