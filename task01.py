n = int(input("Enter a number: "))

s = 0

for i in range(1, 11):
    x = n * i
    print(x, end=" ")

    if i % 2 != 0:
        s = s + x

print()
print("Sum =", s)
print("Square =", s * s)
