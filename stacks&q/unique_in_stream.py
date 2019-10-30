t = 1
while t:
    arr = ['a', "a", 'b', 'c']
    
    m = {}
    q = []
    res = []
    for elem in arr:
        print(m,q)
        try:
            m[elem]
            ind = q.index(elem)
            del q[ind]
            if q:
                res.append(q[0])
            else:
                res.append(-1)
        except KeyError:
            m[elem]=0
            q.append(elem)
            res.append(q[0])
        except Exception as e:
            print(str(e))
    print(*res)
    t -=1