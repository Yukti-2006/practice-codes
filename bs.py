print("Enter 1 for Linear Search")
print("Enter 2 for Binary Search")
m=int(input("Enter your choice(1,2):"))
match m:
    case 1:
        a=[]
        n=int(input("enter no of customer IDs:"))
        for i in range (0,n):
            w=int(input("Enter customer ID:"))
            a.append(w)
        print("Final List:",a)

        search_id=int(input("Enter the ID to search for:"))
        i=0
        for i in range(len(a)):
            if (a[i]!=search_id):
                i=i+1
                print("ID not found")
            else:
                print("ID found at index:",i)
            
              
            
    case 2:
        a=[]
        n=int(input("Enter no of customer IDs:"))
        for i in range(0,n):
            w=int(input("Enter no. of customer IDs:"))
            a.append(w)
        print("Final List:",a)

        search_id=int(input("Enter customer ID to search:"))
        a.sort()
        i=0
        j=len(a)-1
        while(i<=j):
            mid =(i+j)//2
            if a[mid]==search_id:
                print("ID found")
                break
            elif a[mid]<search_id:
                i=mid+1
            else:
                j=mid-1
        else:
            print("ID not found")
    case _:
        print("invalid choice")


        





