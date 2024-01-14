# sort list with index keep original
myList = [2,3,5,1,77,22]
l = [i for i in sorted(enumerate(myList), key=lambda x:x[1])]
print(l)