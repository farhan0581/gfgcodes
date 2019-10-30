
def quicksort(arr, start, end, k):
    # print(arr,start,end)
    if end-start <= 0:
        if end == k:
            # print(arr[end])
            return arr[end]
        return
    pivot = end
    pindex = start
    _s = start
    while start <= end-1:
        if arr[start] < arr[pivot]:
            arr[pindex], arr[start] = arr[start], arr[pindex]
            pindex += 1
        start += 1

    arr[pivot], arr[pindex] = arr[pindex], arr[pivot]
    
    if k == pindex:
        # print(arr[pindex])
        return arr[pindex]
        # return
    elif k > pindex:
        r=quicksort(arr, pindex+1, end, k)  
    elif k < pindex:
        r=quicksort(arr, _s, pindex-1, k)
    
    return r

    # quicksort(arr, _s, pindex-1, k)
    # quicksort(arr, pindex+1, end, k)

arr = [50,23,9,18,61,32, 1,2,44,567]
print(quicksort(arr,0,9, 5))
print(arr)
# [1, 2, 9, 18, 23, 32, 44, 50, 61, 567]