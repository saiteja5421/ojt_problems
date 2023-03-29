# Expected Output : {1: 1, 2: 4, 3: 9, 4: 16, 5: 25} - write a program to get the expected result
c = {}
for i in range(1, 11):
    c[i] = i * i
print(c)
