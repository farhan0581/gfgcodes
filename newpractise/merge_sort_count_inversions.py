'''

Problem statement
For a given integer array/list 'ARR' of size 'N' containing all distinct values, find the total number of 'Inversions' that may exist.

An inversion is defined for a pair of integers in the array/list when the following two conditions are met.

A pair ('ARR[i]', 'ARR[j]') is said to be an inversion when:

1. 'ARR[i] > 'ARR[j]' 
2. 'i' < 'j'

Where 'i' and 'j' denote the indices ranging from [0, 'N').
Detailed explanation ( Input/output format, Notes, Images )
Constraints :
1 <= N <= 10^5 
1 <= ARR[i] <= 10^9

Where 'ARR[i]' denotes the array element at 'ith' index.

Time Limit: 1 sec
Sample Input 1 :
3
3 2 1
Sample Output 1 :
3
Explanation of Sample Output 1:
We have a total of 3 pairs which satisfy the condition of inversion. (3, 2), (2, 1) and (3, 1).
Sample Input 2 :
5
2 5 1 3 4
Sample Output 2 :
4
Explanation of Sample Output 1:
We have a total of 4 pairs which satisfy the condition of inversion. (2, 1), (5, 1), (5, 3) and (5, 4).


Hints:
1. Start with the brute force approach.
2. Use a modified merge sort.
3. Iterate through the elements in sorted order and use a Fenwick tree to track the inversions.

'''
def mergesort(arr, start, end, c):
    if start >= end:
        return c
    
    mid = (start+end)//2
    c = mergesort(arr, start, mid, c)
    c = mergesort(arr, mid+1, end, c)

    return merge(arr, start, mid, end, c)


def _merge(arr, start, mid, end):
    i = start
    j = mid+1

    tmp = []
    while i <= mid and j <= end:
        if arr[i] < arr[j]:
            tmp.append(arr[i])
            i += 1
        else:
            tmp.append(arr[j])
            j += 1
    
    while i <= mid:
        tmp.append(arr[i])
        i += 1
    
    while j <= end:
        tmp.append(arr[j])
        j += 1
    
    
    for i in range(len(tmp)):
        arr[start+i] = tmp[i]


def merge(arr, start, mid, end, cnt):
    i = start
    j = mid+1

    tmp = []
    while i <= mid and j <= end:
        if arr[i] < arr[j]:
            tmp.append(arr[i])
            i += 1
        else:
            tmp.append(arr[j])
            j += 1
            cnt += (mid-i + 1) # here we need to take the range, only this is the required
    
    while i <= mid:
        tmp.append(arr[i])
        i += 1
    
    while j <= end:
        tmp.append(arr[j])
        j += 1
    
    
    for i in range(len(tmp)):
        arr[start+i] = tmp[i]
    
    return cnt


def getInversions(arr, n) :
    # Write your code here.
    c = 0
    return mergesort(arr, 0, n-1, c) 


l = [2, 5, 1, 3, 4, 4, -1, 3 , 100, 9, -200]
l = [2, 5, 1, 3, 4]
print(getInversions(l,len(l)))
print(l)