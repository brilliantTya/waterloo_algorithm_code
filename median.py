def rank(arr, k):
    if len(arr) <= 5:
        return sorted(arr)[k]

    i = 0
    medians = []
    while i + 5 < len(arr):
        medians.append(rank(arr[i: i + 5], 2))
        i += 5
    mofm = rank(medians, len(medians) // 2)
    smaller, larger, equal = [], [], []
    for each in arr:
        if each < mofm:
            smaller.append(each)
        elif each > mofm:
            larger.append(each)
        else:
            equal.append(each)
    if len(smaller) > k:
        return rank(smaller, k)
    elif len(smaller) <= k < len(smaller) + len(equal):
        return mofm
    else:
        return rank(larger, k - len(smaller) - len(equal))

def median(arr):
    return rank(arr, len(arr) // 2)


if __name__ == '__main__':
    arr = [9, 10, 6, 7, 4, 16, 38]
    print(rank(arr, 6))
