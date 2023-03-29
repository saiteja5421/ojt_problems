#  program to interchange first and last elements in a list
b =input("enter the number")
print(b)
a = ["sai", 2, 3, "teja"]
temp = a[-1]
a[-1] = a[0]
a[0] = temp
print(a)
