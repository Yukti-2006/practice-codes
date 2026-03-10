print("Enter 1 for Selection Sort")
print("Enter 2 for Bubble Sort")
m=int(input("Enter your choice(1,2):"))
match m:
    case 1:
        a=[]
        n=int(input("Enter the no. of Employees:"))
        for i in range(0,n):
            w=float(input("Enter the salary:"))
            a.append(w)
        print("Final list:",a)

#Selection Sort
        for i in range(0,n):
            k=i
            for j in range(i+1,n):
                if (a[j]<a[k]):
                    k=j
                    if (k!=i):
                        temp=a[i]
                        a[i]=a[k]
                        a[k]=temp
        print("Sorted List:",a) 


    case 2:
        a=[]
        n=int(input("Enter the no. of Employees:"))
        for i in range(0,n):
            w=float(input("Enter the salary:"))
            a.append(w)
        print("Final list:",a)

#Bubble Sort
        for i in range(1,n):
            for j in range(0,n-i):
                if (a[j]>a[j+1]):
                    a[j],a[j+1]=a[j+1],a[j]
        print("Sorted list:",a)  

    case _:
        print("Invaild Choice!!")          






