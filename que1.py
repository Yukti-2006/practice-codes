n = int(input("Enter the number"))

if n % 9 != 0:
    print(n % 9, end='')

for i in range(n // 9):
    print(9, end='')

print()
