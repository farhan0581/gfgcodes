t = int(1)
while t:
    # n, k = input().split()
    n, k = 10, 4
    n = int(n)
    k = int(k)
    # arr = list(map(int, input().split()))
    arr = [8, 5, 10, 7, 9, 4, 15, 12, 90, 13]
    # arr = [12, 1, 78, 90, 57, 89, 56]

    q = []
    res = []

    for i in range(k):
        while q and arr[i] >= arr[q[-1]]:
            q.pop()
        
        q.append(i)

    for i in range(k, n):
        res.append(arr[q[0]])
        while q and q[0] <= i-k:
            del q[0]
        while q and arr[i] >= arr[q[-1]]:
            q.pop()
        
        q.append(i)

    res.append(arr[q[0]])
    print(*res)
    t -= 1