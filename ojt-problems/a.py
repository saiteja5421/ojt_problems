# # n = 1234 

# # n1 =str(n)
# # num = n1[::-1]
# # num=int(num)
# # print(num)


# # list1 = [1,2,3,4,5,6,7,8,9]
# # list2= []
# # for i in list1:
# #     if i % 2 == 0:
# #         list2.append(i*2)
# #     elif i % 2 !=0:
# #         list2.append(i*3)
# # print(list2)

# t = ("Msys","Technologies","2007")
# l=list(t)
# l.append("Python")
# t1=tuple(l)
# print(t1)
# #########################################

# t = ("Msys", "Technologies", "2007")
# t1 = ("Python",)
# print(t+t1)
# t2 = ("Msys", "Technologies", "2007")
# t3 = ["Python"]
# t4 = list(t2)
# t4.extend(t3)
# print(t4)
 
# s =("Msys", "Technologies", "2007")
# s1 = list(s)
# s1.append('python')
# print(s1)
# #Output:
# ('Msys', 'Technologies', '2007', 'Python')
# ['Msys', 'Technologies', '2007', 'Python']
# ['Msys', 'Technologies', '2007', 'python']


# dict={'India':'New Delhi', 'USA':'Washington D.C.', 'Nepal':'Kathmandu'}
# list_keys=[]
# list_values=[]
# for i,j in dict.items():
#     list_keys.append(i)
#     list_values.append(j)

# print(list_keys)
# print(list_values)

# if "australia" not in list_keys:
#     print("NA")



# n = int(input("Enter a number:"))
# for i in range(1,n+1):
#     print(" " * (n-i),end="")
#     for j in range(i,0,-1):
#         print(j,end="")
#     for k in range(2,i+1):
#         print(k,end="")
#     print()
# for i in range(n-1,0,-1):
#     print(" " * (n-i),end="")
#     for j in range(i,0,-1):
#            print(j,end="")
#     for k in range(2,i+1):
#            print(k,end="")
#     print()


# string = "Hello, welcome to this organisation."
# width = 4
# string=string.replace(" ","")
# # Reverse the string and remove blank spaces
# #string = string[::-1].replace(" ", "")
# # print(string)

# for i in range(0,len(string),4):
#      print(string[i:i+4])

# n = int(input("Enter a number:"))
# count = 0
# for i in range(n+1):
#     if str(1) in str(i):
#         count += str(i).count(str(1))
# print(count)

# s="abcdefg"
# k=2 
# m=s[:k]
# m1=m[::-1]
# n=m1+s[k:]
# print(n) 

# from itertools import permutations 

# string = "abc"

# string_permutations = list(permutations(string))
# string_permutations = ["".join(permutations) for permutations in string_permutations]
# print(string_permutations)
# print(len(string_permutations))


x= 1234 
x=str(x)
x1=x[::-1]
x2=int(x1)
print(x2)

x = 1234 
reverse_x=0
while x != 0:
    d = x%10 
    reverse_x = reverse_x * 10 +d 
    x=x//10 
print(reverse_x)

d ={'Msys Technologies':'Sanjay Sehgal', 'Infosys':'Salil Parekh','TCS':'Rajesh Gopinathan'}
k = sorted(d.items(), key=lambda x : x[1] )
print(dict(k))
k = sorted(d.items())
print(dict (k))


d ={'Msys Technologies':'Sanjay Sehgal', 'Infosys':'Salil Parekh','TCS':'Rajesh Gopinathan'}
k = sorted(d.items(), key=lambda x : x[1] )
print(dict(k))
k = sorted(d.items())
print(dict (k))

class Row():
    def __init__(self,a,b):
        self.a=a
        self.b =b 

row=Row(a=3,b=4)
print(row.a)
print(row.b)