grades= [19,0,67,89,90,76,56]
i=0
for i in range(len(grades)):
    assert grades[i]!=0, "Guy had a bad day"
    if(grades[i]>52):
            print("Pass")
    else:
            print("fail")    
print("Its over")


# a="hello"
# assert a="hello","HEllo chai pilo frnds"