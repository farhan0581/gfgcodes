

def minCoins(den, n):
    coins = 0
    ans = []

    i = len(den)-1

    while n > 0:
        if den[i] > n:
            i -= 1
        else:
            n = n - den[i]
            coins += 1
            ans.append(den[i])
    print(ans)
    
    return coins
            



d =  [1, 2, 5, 10, 20, 50, 100, 500, 1000]
n = 187

print(minCoins(d,n))