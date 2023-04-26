# # try:
# #     with open("file1.txt","a") as file:
# #         b =file.write("Hello World")
# # except :
# #     print("File not found")
    

# # f =open("file1.txt","w")
# # f.write("Hello world")
# # f.close() 

# string = input("Enter the main string:")
# word = input("Enter the string combination you have to know:")
# count = 0
# for i in range(0,len(string)):
#     new_word = string[i:i+len(word)]
#     if "a" in new_word and "b" in new_word and "c" in new_word:
#         print(new_word)
#         count += 1
# print(count)




# l=[1,1,0,1,1,1]
# m=[]
# for i in l:
#     if l[i] and l[i+1]:
#         m.append(l[i])
#     else:
#         m.append(0)
# print(m)


substring="tej"
string="saiteja"
a=string.index(substring)
print(a)
import operator 
print(operator.contains(string,substring))


# l=[1,1,1,1,1,1]
# m=[]
# for i in range(len(l)-1):
#     if l[i] and l[i+1]:
#         m.append(l)
# print(m)

