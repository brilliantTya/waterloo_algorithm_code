from util import swap


def insertionSort(arr):
    for i in range(1, len(arr)):
        for j in range(i):
            if j == 0 and arr[i] < arr[j]:
                arr[: i + 1] = [arr[i]] + arr[: i]
            elif arr[j - 1] < arr[i] <= arr[j]:
                arr[j: i + 1] = [arr[i]] + arr[j: i]
    return arr


if __name__ == '__main__':
    arr = [5, 3, 1, 4, 2]
    print(insertionSort(arr))
