sal=int(input("Enter the salary:"))
gen=input("Enter the gender:")
if(gen=='male'):
    if(sal<10000):
        s=sal*1.07
        print("Salary is",s)
        if(sal>10000):
            s=sal*1.05
            print("Salary is ",s)
elif(gen=='female'):
        if(sal<10000):
            s=sal*1.12
            print("Salary is",s)
        if(sal>10000):
            s=sal*1.1
            print("Salary is",s)