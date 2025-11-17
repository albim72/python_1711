import copy

a = [1, 2, 3, 8, 11, 6, 9, 8, 17, 8]
print(a)
print(type(a))
print(len(a))
print(id(a))
print(a[5])
print(a[7])
print(a[9])

print(id(a[7]))
print(id(a[9]))
print(id(a[5]))

a[8] = True
print(a)
a[1] = "dwa"
print(a)

a.append(21)
print(a)

a.insert(3, 50)
print(a)
# lista Pythona = dynamiczna tablica C z amortyzacją, przechowująca referencje, z nadmiarową pamięcią do szybkiego wzrostu!

b=a[:]
print(b)
print(id(a))
print(id(b))

a[2:5] = [1001,2302,1205,5643]
print(a)
print(b)

c = list(a)
print(c)

print("_"*60)

g = [7,3,9]
h = g[:]
k = list(g)

print(id(g),id(h),id(k)) # shallow copy

g = [[1,3,5], [2,4,6], [7,8,9]]
h = g[:]
# h = list(g)

g[0].append(99)
print(g)
print(h) # efekt płytkiej kopii

#głęboka kopia

g = [[1,3,5], [2,4,6], [7,8,9]]
h = copy.deepcopy(g)
print("_"*60)
g[0].append(99)
print(g)
print(h)

s = 'lajkonik'
print(s)
print(s[0])
print(s[2])
print(s[1:5])
print(s[:5])
print(s[4:])
print(s[-1])
print(s[::-1])
print(s[6:2:-1]) #laj -> s[start:stop:krok]
