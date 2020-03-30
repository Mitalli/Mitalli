student = ['a','b','c']
student.append('D')
print(student)

#student.sort(capital)
#print(student)

student.pop(2)
print(student)

del student[1]
print(student)

#del student
#print('the list has been deleted'+student)

student.append('e')
print(student)

name = 'mitali'
print(name[0:5:2])

#student.clear()
#print(student)

student.sort()
print(student)

student.insert(4,'f')
print(student)

student.insert(6,'z')
print(student)
#print(student[5])

for ref in student:
    print(ref)

age = ['2','5','6']
for x in zip(student,age):
    print(x)

list1 = ['a','b','c']
list2 = ['1','2','3']
list3 = [1,2,3]
list4 = ['umang','sheena','neha','Alaya']
print(list3)
list3.extend(list2)
list1.extend(list3)
print(list1)
print(list4)
list4.sort(reverse = True)
print("after sort" , list4)

