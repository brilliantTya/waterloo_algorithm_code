def longestCommonSeq(str1, str2):
    n, m = len(str1), len(str2)
    if n == 0 or m == 0:
        return ''

    dp = [['' for j in range(m)] for i in range(n)]
    for i in range(n):
        for j in range(m):
            if str1[i] == str2[j]:
                dp[i][j] = dp[i - 1][j - 1] + str1[i]
            else:
                if len(dp[i - 1][j - 1]) > len(dp[i - 1][j]) \
                        and len(dp[i - 1][j - 1]) > len(dp[i][j - 1]):
                    dp[i][j] = dp[i - 1][j - 1]
                elif len(dp[i - 1][j]) > len(dp[i][j - 1]):
                    dp[i][j] = dp[i - 1][j]
                else:
                    dp[i][j] = dp[i][j - 1]

    return dp[n - 1][m - 1]


if __name__ == '__main__':
    str1 = 'snowy'
    str2 = 'sunny'
    print(longestCommonSeq(str1, str2))
