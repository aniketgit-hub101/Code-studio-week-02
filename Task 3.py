n = int(input("Enter N: "))

cnt = 0

for i in range(1, n + 1):
    if i % 2 == 0 and i % 4 != 0:
        print(i, end=" ")
        cnt = cnt + 1

print()
print("Count =", cnt)
