from util import swap


def bubble_sort(arr):
    for i in range(len(arr) - 1):
        swapped = False
        for j in range(0, len(arr) - 1 - i):
            if arr[j] > arr[j + 1]:
                swap(arr, j, j + 1)
                swapped = True
        if not swapped:
            return arr
    return arr


if __name__ == '__main__':
    arr = [5, 3]
    print(bubble_sort(arr))
