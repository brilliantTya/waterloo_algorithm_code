from util import swap


def _quick_sort(arr, i, j):
    if j - i <= 1:
        return arr

    pivot = arr[j - 1]
    lpointer, rpointer = i, j - 2
    while True:
        while lpointer <= rpointer and arr[lpointer] <= pivot:
            lpointer += 1
        while lpointer <= rpointer and arr[rpointer] >= pivot:
            rpointer -= 1
        if lpointer <= rpointer:
            swap(arr, lpointer, rpointer)
        else:
            break
    swap(arr, lpointer, j - 1)
    _quick_sort(arr, i, lpointer)
    _quick_sort(arr, lpointer + 1, j)
    return arr


def quick_sort(arr):
    return _quick_sort(arr, 0, len(arr))


if __name__ == '__main__':
    arr = [2, 3, 4, 2, 0, 1, 3, 2, 4]
    print(quick_sort(arr))
