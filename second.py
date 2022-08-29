# a=3
# # b=3
# # print(id(a))
# # print(id(b))
# b= int(input("Ente the num:"))
# c=a+b
# print(c)

# binn= "kevin"
# print(binn[-1])
# print(type(binn))

# a= 1+22+4+7\
#     -4-4+8\

# print(a)

# if a==34:
#     print("a is 34")
# elif a==35:
#     print ("a is 35")
# else:
#     print("a is some number") 
# print("a is a number")    

# for i in range(333,666):
#     if(i%9 ==0):
#         print(i)


f=9999
l=1000
for n in range(1000,9999):
    flag= True
    for i in range(2,round(n**0.5)):
        if(n%i==0):
            flag=False
            break
    if(flag):
        if(i<f):
            f = i
        elif(i>l):
            l =i
print("first one:"+str(f))  
print("last one:"+str(l))                


        

