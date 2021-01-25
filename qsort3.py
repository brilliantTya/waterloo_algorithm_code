def swap(lst, i, j):
    lst[i], lst[j] = lst[j], lst[i]

def partition3(lst):
    if not lst:
        return lst, 0, 0
    pivot = lst[-1]

    pivot_duplicate = 0
    for i in range(len(lst) - 2, -1, -1):
        if lst[i] == pivot:
            lst.pop(i)
            pivot_duplicate += 1

    l = 0
    r = len(lst) - 2

    while True:
        while l <= r and lst[l] < pivot:
            l += 1
        while l <= r and lst[r] > pivot:
            r -= 1

        if l <= r:
            swap(lst, l, r)
        else:
            break
    
    swap(lst, l, len(lst) - 1)
    return lst[:l] + [pivot] * pivot_duplicate + lst[l:], l, l + pivot_duplicate + 1

def qsort3(lst, start, end):
    if end - start <= 1:
        return lst

    lst[start:end], bp1, bp2 = partition3(lst[start:end])
    bp1 += start
    bp2 += start
    qsort3(lst, start, bp1)
    qsort3(lst, bp2, end)

    return lst

    
# lst = [2, 4, 2, 4, 3, 5, 6, 3, 5, 6, 3]
# print(qsort3(lst, 0, len(lst)))
