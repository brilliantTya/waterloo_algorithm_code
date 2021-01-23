def _maximalSubarray(arr, i, j):
    if j - i == 0:
        return 0, i, j
    if j - i == 1:
        return (0, i, i) if arr[0] <= 0 else (arr[0], i, j)

    c = (i + j) // 2
    left, lefti, leftj = _maximalSubarray(arr, i, c)
    right, righti, rightj = _maximalSubarray(arr, c, j)
    crossi, crossj = c, c
    curri, currj = c - 1, c
    maxleft, maxright = 0, 0
    sumleft, sumright = 0, 0

    while curri >= 0:
        sumleft += arr[curri]
        if sumleft > maxleft:
            crossi = curri
            maxleft = sumleft
        curri -= 1
    while currj < len(arr):
        sumright += arr[currj]
        if sumright > maxright:
            crossj = currj
            maxright = sumright
        currj += 1

    cross = maxleft + maxright
    maxx = max(cross, left, right)

    if maxx == cross:
        return maxx, crossi, crossj
    elif maxx == left:
        return maxx, lefti, leftj
    elif maxx == right:
        return maxx, righti, rightj

def maximalSubarray(arr):
    return _maximalSubarray(arr, 0, len(arr))


if __name__ == '__main__':
    arr = [-9, 3, 7, 8, -10, 3, 8, 15, 4, -38]
    print(maximalSubarray(arr))
