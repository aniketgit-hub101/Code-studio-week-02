a = [10, 20, 30, 40, 50]
key = 30

found = 0

for i in range(len(a)):
    if a[i] == key:
        found = 1

if found == 1:
    print("Found")
else:
    print("Not Found")
