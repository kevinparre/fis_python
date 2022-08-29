from collections import Counter
resu={}
str="eeororoeroeoreoroefmefemfekrefekfek"
print(str.count('e'))
res=str.replace("e","z")
print(res)
resu=Counter(str)
# print(resu)
for i in resu.keys():
    print(i)
    print(resu[i])
    if(resu[i]>2):
        result=str.replace(i,"p")
print(result)

