import math
from copy import copy


def swap(arr, i, j):
    arr[i], arr[j] = arr[j], arr[i]


def eucliean(a: tuple, b: tuple):
    return math.sqrt((a[0] - b[0])**2 + (a[1] - b[1])**2)


def _binary_search(arr, i, j, target):
    if j - i <= 1:
        return i

    c = (i + j) // 2
    if arr[c] > target:
        return _binary_search(arr, i, c, target)
    elif arr[c] == target:
        return c
    else:
        return _binary_search(arr, c, j, target)


def binary_search(arr, target):
    return _binary_search(arr, 0, len(arr), target)


def _sort_points(arr, i, j, by='y'):
    if j - i <= 1:
        return arr

    if by == 'y':
        axis = 1
    elif by == 'x':
        axis = 0

    pivot = arr[j - 1][axis]
    lpointer, rpointer = 0, j - 2
    while True:
        while lpointer <= rpointer and arr[lpointer][axis] <= pivot:
            lpointer += 1
        while lpointer <= rpointer and arr[rpointer][axis] >= pivot:
            rpointer -= 1
        if lpointer < rpointer:
            swap(arr, lpointer, rpointer)
        else:
            break
    swap(arr, lpointer, j - 1)
    _sort_points(arr, i, lpointer, by=by)
    _sort_points(arr, lpointer, j, by=by)
    return arr


def sort_points(arr, by='y'):
    return _sort_points(arr, 0, len(arr), by=by)


def rank_points(arr, k, by='y'):
    if len(arr) <= 5:
        return sort_points(arr, by=by)[k]

    if by == 'y':
        axis = 1
    elif by == 'x':
        axis = 0

    i = 0
    medians = []
    while i + 5 < len(arr):
        medians.append(rank_points(arr[i: i + 5], 2, by='x'))
        i += 5

    mofm = rank_points(medians, len(medians) // 2, by=by)
    smaller, equal, larger = [], [], []
    for each in arr:
        if each[axis] < mofm[axis]:
            smaller.append(each)
        elif each[axis] > mofm[axis]:
            larger.append(each)
        else:
            equal.append(each)

    if len(smaller) > k:
        return rank_points(smaller, k, by=by)
    elif len(smaller) <= k < len(smaller) + len(equal):
        return mofm
    else:
        return rank_points(larger,
                           k - len(smaller) - len(equal), by=by)


def _binary_search_points(arr, i, j, target, by='y'):
    if j - i <= 1:
        return i

    if by == 'y':
        axis = 1
    elif by == 'x':
        axis = 0

    c = (i + j) // 2
    if arr[c][axis] < target:
        return _binary_search_points(arr, c, j, target, by=by)
    elif arr[c][axis] == target:
        return c
    else:
        return _binary_search_points(arr, i, c, target, by=by)


def binary_search_points(arr, target, by='y', sort=False):
    sorted_arr = copy(arr)

    if sort:
        sorted_arr = sort_points(arr, by=by)
    return _binary_search_points(sorted_arr, 0, len(arr),
                                 target, by=by)


def _sort_tuple_value_pair(arr, by='y'):
    if len(arr) <= 1:
        return arr

    if by == 'y':
        axis = 1
    elif by == 'x':
        axis = 0

    c = len(arr) // 2
    left = _sort_tuple_value_pair(arr[:c], by=by)
    right = _sort_tuple_value_pair(arr[c:], by=by)
    out = []
    while len(left) > 0 and len(right) > 0:
        if left[0][0][axis] <= right[0][0][axis]:
            out.append(left.pop(0))
        else:
            out.append(right.pop(0))

    out += left + right
    return out


def sort_tuple_value_pair(arr, by='y'):
    return _sort_tuple_value_pair(arr, by=by)


if __name__ == '__main__':
    arr = [0, 2]
    print(binary_search(arr, 1))
