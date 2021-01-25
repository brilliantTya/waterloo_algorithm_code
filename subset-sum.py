def subset_sum(arr, target):
    '''
    dp[i][j]: whether there is a subset in arr[i:] that add up to j
    recurrence: dp[i][j] = dp[i + 1][j] or dp[i + 1][j - arr[i]]
    return: dp[0][target]
    '''
    n = len(arr)
    if n == 0:
        return True if target == 0 else False

    dp = [[0 for j in range(target + 1)] for i in range(n)]

    if arr[-1] <= target:
        dp[-1][arr[-1]] = 1
    for i in range(n):
        dp[i][0] = 1

    for i in range(n - 2, -1, -1):
        for j in range(target + 1):
            if arr[i] <= j:
                dp[i][j] = dp[i + 1][j] or dp[i + 1][j - arr[i]]
            else:
                dp[i][j] = dp[i + 1][j]

    return True if dp[0][target] else False


if __name__ == '__main__':
    arr = [2, 3, 4, 1, 0, 1, 7, 9, 6]
    print(subset_sum(arr, 13))
