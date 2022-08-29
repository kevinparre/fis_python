# a=(1,2,"Kevin",5.69,[1,2,34,5])
# b=a
# print(b)
# print(type(a))
# c,d,e,f,g =a
# print(g)

place="  pune   "
place2=place[::-1]
if (place == place2):
    print("Palindrome")
else:
    print("Not Palindrome")    
print(place2)
place3= place.strip()
print(place3)
print(place3.capitalize())
print(place3.upper())
str="i am from {}"
print(str.format(place3))