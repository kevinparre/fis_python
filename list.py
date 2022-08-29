# a=[2,"kevin",7,9.99,0]
# for x in range(len(a)):
#     print(a[x])

grades=[33,45,67,5,6,77,33,67,77]
grades.append(66)
a=[1,2,3,4,5]
b=[5,67,8,90,6]
c=a+b
a.extend(b)
print(a)
print(b)
print(c)
print(b.count(5))

b.remove(90)
print(b)

a.pop(1)
print(a)

a[3]=99
print(a.index(99))

unique_grades= list(dict.fromkeys(grades))

unique_grades.insert(4,99)
print(unique_grades)

s=sum(grades)
print(s)

m=1
for i in grades:
    m=m*i
print(m)    