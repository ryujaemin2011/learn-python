dic = {'name': 'jae', 'phone': '0192458', 'birth': '1111'}
print(dic['name'])
a = {1:'a'}
a[2] = 'b'
print(a)
del a[1]
print(a)
print(a.keys())
print(a.values())
print(a.items())
a.clear()
print(a)
print(a.get(1))
print(a.get(1, '없음'))
print(1 in a)