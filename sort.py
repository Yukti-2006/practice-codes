print("enter 1 for Bubble Sort")
print("enter 2 for Selection Sort")

x=int(input("enter the choice(1,2): "))
match x:
    case 1:
        a = []
        n = int(input("Enter the number of elements: "))

        for i in range(n):
            w = int(input("Enter element: "))
            a.append(w)

        print("Original list:", a)

# Bubble Sort logic
        for i in range(n - 1):
            for j in range(n - 1 - i):
                if a[j] > a[j + 1]:
                    a[j], a[j + 1] = a[j + 1], a[j]

        print("Sorted list using Bubble Sort:", a)

    case 2:
        a = []
        n = int(input("Enter the number of elements: "))

        for i in range(n):
            w = int(input("Enter element: "))
            a.append(w)

        print("Original list:", a)

# Selection Sort logic
        for i in range(n):
            min_index = i
            for j in range(i + 1, n):
                if a[j] < a[min_index]:
                    min_index = j
                    a[i], a[min_index] = a[min_index], a[i]

        print("Sorted list using Selection Sort:", a)

    case _:
        print("Invalid Choice")