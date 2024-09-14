# Strings
a = "HEllo"
t = "World"
u = a+t
print(type(u))
print(u)
print(u[9])


# Lists
l = [1,2,3,4,5,7,8,8]
print(type(l))
l.append(100)
print(l)
l[2] = 'Hello'
print(l)


# Tuples
T = (1,2,3,4,5,6,7,8,99)
#These two ops will not be performed as a tuple is immutable
# print(T[3])
# T.append(100)
# T[5] = 'dead'
# print(T)


# Dictionary
d = dict()
d['new'] = 'zero'
d['newer'] = 'One'
d['newest'] = 'Two'
d['brand_new'] = 'Three'
print(d)
d['new'] = 'qwas'
print(d['new'])


# SEts
s = {2,3,4}
s.add(5)
s.add(5)
s.add(5)
s.remove(5)
s.add(5)
s.add(6)
s.add(1)
print(s)

