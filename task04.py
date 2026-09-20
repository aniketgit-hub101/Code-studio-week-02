n = int(input("Enter the number of elements: "))

a = []

for i in range(n):
    x = int(input("Enter element: "))
    a.append(x)

s = 0

for i in range(0, n, 2):
    print(a[i], end=" ")
    s = s + a[i]

print()
print("Sum =", s)
