a={1,2,"Kevin",5.69,True,False}
b={3.14,"GG","Kevin",False,3,(2,3,4,5)}
print(a.difference(b))
print(b.difference(a))
# a.remove("l")
a.discard("k")
print(a)
print(a.intersection(b))
a.pop()
a.clear()
print(a)