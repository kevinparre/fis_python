f=open("C:\\Users\Administrator\\Desktop\\text.txt",'r')
g=open("C:\\Users\Administrator\\Desktop\\text_pune.txt",'w')
h=open("C:\\Users\Administrator\\Desktop\\text_dehu.txt",'w')
i=open("C:\\Users\Administrator\\Desktop\\text_other.txt",'w')

line2=g.writelines("ID" +" "*9 +"Name" +" "*15+"Location" +" "*4+"O-Salary" +" "*5+"email" +" "*20+"N-Salary" +" "*5)
line2=g.writelines("\n")
line2=g.writelines("------------------------------------------------------------------------------------------------")

line3=h.writelines("ID" +" "*9 +"Name" +" "*15+"Location" +" "*4+"O-Salary" +" "*5+"email" +" "*20+"N-Salary" +" "*5)
line3=h.writelines("\n")
line3=h.writelines("------------------------------------------------------------------------------------------------")

line4=i.writelines("ID" +" "*9 +"Name" +" "*15+"Location" +" "*4+"O-Salary" +" "*5+"email" +" "*20+"N-Salary" +" "*5)
line4=i.writelines("\n")
line4=i.writelines("------------------------------------------------------------------------------------------------")


line=f.readline()

# counter=0
# salarys=[]

while line:
    # counter+=1
    line2=g.writelines("\n")
    line3=h.writelines("\n")
    line4=i.writelines("\n")

    n_salary=0
    salary=int(line[31:37].strip())
    location=line[20:30].strip()
    email=line[5:9]+line[20:23]+"@fisglobal.com"
    id=line[:5]
    name=line[5:20]

    if(location.startswith("Pune")):
        n_salary=salary+(.1 * salary)
        line2=g.writelines(id +" "*5 +name +" "*5+location +" "*8+ str(salary) +" "*7+email +" "*5+str(n_salary) +" "*5)
    elif(location.startswith("Dehu")):
        n_salary=salary+(.15 * salary) 
        line2=h.writelines(id +" "*5 +name +" "*5+location +" "*8+ str(salary) +" "*7+email +" "*5+str(n_salary) +" "*5)
    elif(location.startswith("Bangalore")):
        n_salary=salary+(.20 * salary) 
        line2=h.writelines(id +" "*5 +name +" "*5+location +" "*8+ str(salary) +" "*7+email +" "*5+str(n_salary) +" "*5)
    else:
        n_salary=salary+(.15 * salary)
        line2=i.writelines(id +" "*5 +name +" "*5+location +" "*8+ str(salary) +" "*7+email +" "*5+str(n_salary) +" "*5)    
    line=f.readline()


f.close()   
g.close()
h.close()
i.close()