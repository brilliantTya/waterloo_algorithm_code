from util import binary_search


def longest_increasing_subseq(arr):
    '''
    dp[i]: best position to start an increasing sequence of length i,
           where best means the rearest. Because dp -> [1..max] is sorted in
           ascending order, we can use binary search to find the best.
    '''
    dp = [float('inf'), arr[-1]]
    for i in range(len(arr) - 2, -1, -1):
        if arr[i] < dp[-1]:
            dp.append(arr[i])
        else:
            dp.reverse()
            j = binary_search(dp, arr[i])
            dp[j] = arr[i]
            dp.reverse()
    return len(dp) - 1


if __name__ == '__main__':
    arr = [5, 3, 10, 9, 6, 8, 7, 4, 1, 12, 6]
    print(longest_increasing_subseq(arr))
