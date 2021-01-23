from copy import copy


def _inservionPairs(arr, i, j):
    if j - i == 0:
        return [], 0, []
    if j - i == 1:
        return [arr[i]], 0, []

    c = (i + j) // 2
    left, lcount, lpairs = _inservionPairs(arr, i, c)
    right, rcount, rpairs = _inservionPairs(arr, c, j)
    pairs = lpairs + rpairs
    count = lcount + rcount
    out = []
    rlength, rcopy = len(right), copy(right)

    while len(left) > 0 and len(right) > 0:
        if left[0] <= right [0]:
            out.append(left.pop(0))
        else:
            this = right.pop(0)
            out.append(this)
            count += len(left)
            for each in left:
                pairs.append((each, this))

    out += left + right

    return out, count, pairs

def inversionPairs(arr):
    return _inservionPairs(arr, 0, len(arr))


if __name__ == '__main__':
    arr = [10, 7, 9, 2, 7, 5, 4, 8]
    print(inversionPairs(arr))
