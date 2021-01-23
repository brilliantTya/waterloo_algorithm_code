from util import sort_points, sort_tuple_value_pair, binary_search_points


def _weighted(arr):
    '''
    arr: array of tuples ((start, end), value)
    dp[i]: maximum sum of value in arr[i:]
    recurrence: dp[i] = max(dp[next(i)] + arr[i][1], dp[i + 1])
    return: dp[0]
    '''
    if len(arr) == 0:
        return 0

    dp = [0 for _ in range(len(arr))]
    sorted_arr = sort_tuple_value_pair(arr, by='x')
    dp[-1] = sorted_arr[-1][1]
    sorted_intervals = [each[0] for each in sorted_arr]
    print(sorted_intervals)

    next_compatible = [binary_search_points(sorted_intervals,
                       interval[1], by='x') + 1
                       for interval in sorted_intervals]
    print(next_compatible)

    for i in range(len(sorted_intervals) - 2, -1, -1):
        if next_compatible[i] < len(sorted_intervals):
            dp[i] = max(dp[next_compatible[i]] + sorted_arr[i][1], dp[i + 1])
        else:
            dp[i] = max(sorted_arr[i][1], dp[i + 1])
    return dp[0]


def _nonweighted(arr):
    if len(arr) < 1:
        return []

    arr = sort_points(arr)
    chosen = [arr[0]]
    for interval in arr[1:]:
        if interval[0] >= chosen[-1][1]:
            chosen.append(interval)
    return chosen


def intervalScheduling(arr, weighted=False):
    if weighted:
        return _weighted(arr)
    else:
        return _nonweighted(arr)


if __name__ == '__main__':
    arr = [((2, 5), 9), ((3, 7), 10), ((4, 10), 25), ((1, 1), 2),
           ((0, 9), 20), ((1, 6), 17), ((3, 5), 6), ((2, 4), 5), ((4, 5), 1)]
    print(intervalScheduling(arr, weighted=True))
