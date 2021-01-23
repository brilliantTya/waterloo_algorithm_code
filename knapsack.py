import numpy as np


def knapsack(arr, capacity: int):
    '''
    dp[i][j]: maximum value from arr[i:] with j capacity left
    recurrence: dp[i][j] = max(dp[i + 1][j],
                               dp[i + 1][j - arr[i][1]] + arr[i][1])
    return dp[0][capacity]
    '''
    n = len(arr)
    if n < 1:
        return 0
    dp = [[0 for j in range(capacity + 1)] for i in range(n)]

    for j in range(arr[-1][1], capacity + 1):
        dp[-1][j] = arr[-1][0]

    for i in range(n - 2, -1, -1):
        for j in range(capacity + 1):
            if arr[i][1] <= j:
                dp[i][j] = max(dp[i + 1][j], dp[i + 1][j - arr[i][1]]
                               + arr[i][0])

    return dp[0][capacity]


if __name__ == '__main__':
    arr = [(2, 5), (3, 7), (4, 10), (1, 1), (0, 9), (1, 6), (3, 5), (2, 4),
           (4, 5)]
    print(knapsack(arr, 15))
