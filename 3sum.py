def binary_search(sorted_lst, target):
    left = 0
    right = len(sorted_lst) - 1
    while left <= right:
        mid = (left + right) // 2
        if sorted_lst[mid] == target:
            return mid
        elif sorted_lst[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return None

def two_sum(sorted_lst, target):
    left = 0
    right = len(sorted_lst) - 1
    while left < right:
        if sorted_lst[left] + sorted_lst[right] == target:
            return sorted_lst[left], sorted_lst[right]
        elif sorted_lst[left] + sorted_lst[right] < target:
            left += 1
        else:
            right -= 1
    return -1, -1

def three_sum1(lst, target):  # O(n^3), brutal force
    ans = []
    for i in range(len(lst)):
        for j in range(i + 1, len(lst)):
            for k in range(j + 1, len(lst)):
                if lst[i] + lst[j] + lst[k] == target:
                    ans.append((lst[i], lst[j], lst[k]))
    return ans

def three_sum2(lst, target):  # O(n^2logn), 1 sum problem
    ans = []
    lst.sort()
    for i in range(len(lst)):
        for j in range(i + 1, len(lst)):
            temp = binary_search(lst[j + 1:], target - lst[i] - lst[j])
            if temp is not None:
                ans.append((lst[i], lst[j], lst[j + 1:][temp]))
    return ans

def three_sum3(lst, target):  # Best we do, O(n^2)
    ans = []
    lst.sort()
    for i in range(len(lst) - 2):
        new_target = target - lst[i]
        a, b = two_sum(lst[i + 1:], new_target)
        if a != -1:
            ans.append((lst[i], a, b))
    return ans


print(three_sum3([1,2,3,4,5,6], 13))

