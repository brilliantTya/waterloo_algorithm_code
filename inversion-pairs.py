def _inversion_pairs(arr, i, j):
    if j - i == 0:
        return [], 0, []
    if j - i == 1:
        return [arr[i]], 0, []

    c = (i + j) // 2
    left, lcount, lpairs = _inversion_pairs(arr, i, c)
    right, rcount, rpairs = _inversion_pairs(arr, c, j)
    pairs = lpairs + rpairs
    count = lcount + rcount
    out = []

    while len(left) > 0 and len(right) > 0:
        if left[0] <= right[0]:
            out.append(left.pop(0))
        else:
            this = right.pop(0)
            out.append(this)
            count += len(left)
            for each in left:
                pairs.append((each, this))

    out += left + right

    return out, count, pairs


def inversion_pairs(arr):
    return _inversion_pairs(arr, 0, len(arr))


if __name__ == '__main__':
    arr = [10, 7, 9, 2, 7, 5, 4, 8]
    print(inversion_pairs(arr))
