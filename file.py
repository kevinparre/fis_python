f=open("C:\\Users\Administrator\\Desktop\\text.txt",'r')
line=f.readline()
print(line.split(" "))
counter=0
while line:
    counter+=1

    print("Record Number : ",counter)
    print("Record ID : ",line[:5])
    print("Record Name : ",line[5:20])
    print("Record Location : ",line[20:30])
    print("Record Salary : ",line[31:])
    print("*****************************")
    # print(line)
    line=f.readline()
print("Total Records: ",counter)    
print("*******All Records Processed!!*********")
# print(line[12:34])
# print(type(line))
# print(len(line))

f.close()   