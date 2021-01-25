import numpy as np


def edit_distance(str1, str2):
    n, m = len(str1), len(str2)
    dp = [[float('inf') for j in range(m + 1)] for i in range(n + 1)]

    for i in range(n + 1):
        dp[i][0] = i
    for j in range(n + 1):
        dp[0][j] = j

    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if str1[i - 1] == str2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1]
            else:
                dp[i][j] = min(dp[i][j - 1], dp[i - 1][j],
                               dp[i - 1][j - 1]) + 1

    print(np.array(dp))
    return dp[-1][-1]


if __name__ == '__main__':
    str1 = 'snowy'
    str2 = 'sunny'
    print(edit_distance(str1, str2))
