def findSecondLargest(arr):
    # Write your code here.
    max=smax=-999999999999
    for i in range(len(arr)):
        if arr[i] > max:
            if smax != max:
                smax = max
            max = arr[i]

        elif arr[i] > smax and arr[i] < max:
            smax = arr[i]
    if smax == -999999999999:
        return -1
    return smax

l=[1,1,1,1]
print(findSecondLargest(l))