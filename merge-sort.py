def merge(sorted1, sorted2):
    out = []
    while len(sorted1) > 0 and len(sorted2) > 0:
        if sorted1[0] <= sorted2[0]:
            out.append(sorted1.pop(0))
        else:
            out.append(sorted2.pop(0))
    out += sorted1 + sorted2
    return out

def _mergeSort(arr, i, j):
    if j - i == 0:
        return []
    if j - i == 1:
        return [arr[i]]

    c = (i + j) // 2
    left = _mergeSort(arr, i, c)
    right = _mergeSort(arr, c, j)
    return merge(left, right)

def mergeSort(arr):
    return _mergeSort(arr, 0, len(arr))


if __name__ == '__main__':
    arr = [2, 3, 4, 2, 0, 1, 3, 2, 4]
    print(mergeSort(arr))
