print("hello I there") # this is the comment
print("""i am new in the project""")
print(""""hi I am another one""")

x= 4
x=9
print(x)

x= 5
x= "Mitali"
print(x)

y = 33333333
y = 'babes'
print(y)

x = 1
print(5+x)
y='in room'
print("yes i am here "+y )
print("""
""")

z= "i am global variable"
def g():
    global z
    z= "I am a local of the local"
    print("I am local variable of the function myfun "+z)
g()
print("Finally out of the loop "+z)

x = {"name": "ABC","age":"5"}
print(x)