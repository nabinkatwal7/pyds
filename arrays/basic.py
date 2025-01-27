import array

myarr = [1, 2, 3, 4, 5]

for x in myarr:
    print(x)

myarr[0] = 10
print(myarr)

myarr.append(6)
print(myarr)

myarr.remove(6)
print(myarr)

myarr.pop()
print(myarr)

print(len(myarr))

print(myarr.count(5))

myarr.sort()
print(myarr)

myarr.reverse()
print(myarr)

newarr = array.array('i', [1, 2, 3, 4, 5])
print(newarr)