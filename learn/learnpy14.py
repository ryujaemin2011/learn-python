#리스트
odd= [1, 3, 5, 7, 9]
print(odd[0])
print(odd[1] + odd[3])
a = [1, 2, 3, ['a', 'b', 'c']]
print(a[3])
print(a[3][1])
a = [1,2,3,4,5]
print(a[1:4])
a = [1,2,3]
b = [4,5,6]
print(a+b)
print(a*3)
print(len(a))
a[2] = 4
print(a)
del a[1]
print(a)
a.append(5)
print(a)
a = [1,8,3,5,8,3]
print(a)
a.sort()
print(a)
a.reverse()
print(a)
print(a.index(8))
a.insert(2,9)
print(a)
a.remove(8)
print(a)
print(a.pop())
print(a)
a = [1,1,2,5,3,6]
print(a.count(1))
a.extend([7,8,9])
print(a)