a = "Mitali"
print(a)
print(""" Name
""")

b = "12456"
print(b)
print(type(b))
print(""" String
""")

c= 1145
print(c)
print(type(c))
print(""" Int
""")

d= bytearray(7)
print(d)
print(type(d))
print(""" No idea
""")

e= range(15)
print(e)
print(type(e))
print(""" No idea
""")

f=g=h=30
print(f,g,h)
print(""" Multiple assignment
""")

i=25
print(i)
j=5
k=6
i=4
print(i,j,k)
print(""" Multiple assignment
""")


name = "mitali"
print(name[4])
print(name[5])
print(name[0:5])
print(name[:])
print(name[::])
print(name[:+1:-1])
print(name[:-4])
print(name[::-1])
print(""" Array
""")


l = h
print(bool(l))

date  = (14,0o3,2020)
print("Date is %i/%i/%i"%date)

p = ("New","Learning")
print(p)
print(type(p))

q =frozenset({"a","b","c"})
print(q)
print(type(q))

r = memoryview(bytes(5))
print(r)

s = memoryview(bytearray(5))
print(s)

t = {"{'a','b'}"}
print(t)
print(type(t))

z = 2E3
print(z)
print(type(z))