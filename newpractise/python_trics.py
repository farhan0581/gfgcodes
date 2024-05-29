# sort list with index keep original
myList = [2,3,5,1,77,22]
l = [i for i in sorted(enumerate(myList), key=lambda x:x[1])]
print(l)

l = [i for i in sorted(enumerate(myList), key=lambda x:x[1])]

m = {"farhan":30, "ilma":21, "faizan": 27, "hamdan":1}
m = {k:v for k,v in sorted(m.items(), key=lambda x:x[0], reverse=True)}
print(m)