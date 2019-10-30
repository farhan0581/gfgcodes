# https://practice.geeksforgeeks.org/problems/minimum-cost-path/0/?track=md-graph&batchId=144
t = int(1)
while t:
    
    n = int(input())
    lst = [int(i) for i in input().split()]
    k=0
    arr=[]
    for i in range(n):
        arr.append(lst[k:k+n])
        k=k+n
    
    p = n-1
    q = n-1
    i = j = 0
    cost = arr[i][j]
    cur = arr[i][j] 
    visited = [[None for i in range(n)] for i in range(n)]
    visited[i][j] = True
    while True:
        if i == p and j == q:
            print(cost)
            break
        
        top = (999999999, None, None)
        bottom = (999999999, None, None)
        left = (999999999, None, None)
        right = (999999999, None, None)
        
        if i +1 < n and not visited[i+1][j]:
            bottom = (arr[i+1][j], 1, i+1, j)
        
        if i-1 >= 0 and not visited[i-1][j]:
            top = (arr[i-1][j],4,  i-1, j)
        
        if j+1 < n  and not visited[i][j+1]:
            right = (arr[i][j+1],2, i, j+1)
        
        if j-1 >= 0  and not visited[i][j-1]:
            left = (arr[i][j-1],3, i, j-1)
        
        _min = min(top, bottom, left, right)
        cost += _min[0]
        i = _min[2]
        j = _min[3]
        visited[i][j] = True

    t -= 1