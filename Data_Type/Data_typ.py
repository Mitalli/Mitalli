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

d= a[5]
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
print(name[:-6])
print(name[::-1])
print(""" Array
""")



x= "  Hello, World  "
print(x.strip())
print(x.split(","))
print(x.replace("Hello","i"))

y=2
z=5.5
x = z//y
print(x)

set1 = {"a", "b" , "c"}
set2 = {1, 2, 3,5}
set77 = {5,6,7,1,2,3}

set3 = set1.union(set2)
set4 = set1.copy()
set1.discard("a")
print(set1)
set9 = set2.intersection(set77)
set10 = set77.union(set2)
#set6 = set77.add(8)
#set77.add(8)
set8 = set77.difference(set2)
set77.difference_update(set2)
print(set3)
print(set4)
#print(set5)
print(set77)
print(set8)
print(set9)
print(set10)

