# di={"name":"kevin","age":"21","dept":["CS","IT","Mech"]}
# print(di)
# for x in di:
#    print(di[x]) 
# for i in di.keys():
#     print(i)   
# for i in di.values():
#     print(i) 
# for i,j in di.items():
#     print(i,":",j)
    
# di["university"]="SPPU"
# print(di)  

# di.pop("age")
# print(di) 
# di.__delitem__("kevin")
# print(di)

#1

# d=dict()
# for x in range(5,11):
#     d[x]=x**2
# print(d)

#2
# n=list(d.keys())
# s=list(d.values())
# print(n)
# print(s)

#3

# dict3=dict(zip(n,s))
# print(dict3)

#4

# n=10
# for i in range(n):
#     for j in range(n-i-1):
#         print(" ",end ="")
#     for k in range(2*i +1):
#         print('*',end="") 
#     print()       

 #5
# for i in range(1,100):
#     if(i %7 == 0):
#         print("I am perfect")
#     elif ('7' in str(i)):
#         print("I am perfect")
#     else:
#         print(i)    

#6
# l=0
# for i in range(5):
#     n=int(input("enter the number: "))
#     if(n>l):
#         l=n
# print("the largest number is: ",l)        


#7
# res=dict()
# l=[2,3.14,True,"kevin",'d']
# ty=list()
# for i in l:
#     t=type(i)
#     ty.append(str(t))
# res=dict(zip(l,ty))
# print(res)    


#8
# stock={"apple":20,"orange":10,"pears":10}
# rates={"apple":78,"orange":40.5,"pears":55, "banana":10}
# order= {"apple":3,"orange":7,"pears":6,"pineapple":2}

# cost={}
# for  i in order.keys():
#     if stock.get(i):
#         q=order.get(i)
#         if q<=stock.get(i):
#            cost[i] =q*rates.get(i)
#            stock.update({i:stock.get(i)-q})
#         else:
#             cost[i]=0
# print("Final Cost:")
# print(cost)
# print("Remaining stock:")
# print(stock)           





