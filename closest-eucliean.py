from util import eucliean, sort_points, rank_points


def closest_eucliean(arr):
    if len(arr) <= 1:
        return float('inf'), (None, None)
    if 1 < len(arr) <= 12:
        closest = float('inf')
        group = (None, None)
        for i in range(len(arr)):
            for j in range(len(arr)):
                if i != j:
                    temp = eucliean(arr[i], arr[j])
                    if temp < closest:
                        closest = temp
                        group = (arr[i], arr[j])
        return closest, group

    x_median = rank_points(arr, len(arr) // 2, by='x')
    left, right = [], []
    for each in arr:
        if each[0] <= x_median[0]:
            left.append(each)
        else:
            right.append(each)

    lclosest, lgroup = closest_eucliean(left)
    rclosest, rgroup = closest_eucliean(right)
    if lclosest <= rclosest:
        closest = lclosest
        group = lgroup
    else:
        closest = rclosest
        group = rgroup

    candidates = []
    for each in arr:
        if abs(each[0] - x_median[0]) <= closest:
            candidates.append(each)

    sorted_candidates = sort_points(candidates)
    i = 0
    while i < len(candidates):
        currclosest, currgroup = closest_eucliean(sorted_candidates[i:
                                                  min(len(arr), i + 12)])
        if currclosest < closest:
            closest = currclosest
            group = currgroup
        i += 12
    return closest, group


if __name__ == '__main__':
    arr = [(2, 5), (3, 7), (4, 10), (1, 1), (0, 9), (1, 6)]
    print(closest_eucliean(arr))
