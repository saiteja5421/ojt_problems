
# 1. Write a program to reverse a number without using any inbuilt function
n = 1234 
n1=str(n)
num = n1[::-1]
num=int(num)
print(num)
##############################################
number = int(input("enter the number: "))
rev_num=0
while number != 0:
	rev_num = rev_num * 10 + number % 10 
	number //= 10
print(f"After reversed number is {rev_num}")
#Output: After reversed number is 321
# 2. Given a list of first 10 natural numbers, write a program to find the square of all even numbers  and cube of all odd numbers and store them in another list
numbers = [1,2,3,4,5,6,7,8,9,10]  
result_square = []
result_cube = [] 
for num in numbers:                     	
    if num % 2 == 0:
        square = num ** 2           	
        result_square.append(square)   	
    else:                               	
        cube = num ** 3                 	
        result_cube.append(cube)             	
 
print("square root of even no:", result_square)   
print("cube root of odd no:", result_cube)
#Output:
# square root of even no: [4, 16, 36, 64, 100]
# cube root of odd no: [1, 27, 125, 343, 729]
# 3. Given a tuple (“Msys”, “Technologies”, “2007”), add “Python” at the end of this tuple and the  output should also be in the form of tuple. Make a note that tuples are immutable in nature so you  need to find some idea to make modifications and print the updated tuple.
t = ("Msys","Technologies","2007")
l=list(t)
l.append("Python")
t1=tuple(l)
print(t1)
# 4. In the dictionary {‘India’:’New Delhi’, ‘USA’:’Washington D.C.’, ‘Nepal’:’Kathmandu’} list out  all the keys in a list named as ‘list_keys’ and list out all the values in a list named as ‘list_values’.  Also find out the value of key ‘Australia’ in the list and as it is not existing in the list print ‘NA’ as  its value.
# Ans:- 

my_dict = {'India': 'New Delhi', 'USA': 'Washington D.C.', 'Nepal': 'Kathmandu'}
list_keys = list(my_dict.keys())
print("Keys: ", list_keys)
list_values = list(my_dict.values())
print("Values: ", list_values)
value = my_dict.get('Australia', 'NA')
print("Value of 'Australia': ", value)
# 5. Given a dictionary {‘Msys Technologies’:’Sanjay Sehgal’, ‘Infosys’:’Salil Parekh’,  ‘TCS’:’Rajesh Gopinathan’, ‘Wipro’:’Thierry Delaporte’} make a list of all the values associated  with keys in alphabetically sorted order.
 
d ={'Msys Technologies':'Sanjay Sehgal', 'Infosys':'Salil Parekh','TCS':'Rajesh Gopinathan'}
k = sorted(d.items(), key=lambda x : x[1] )
print(dict(k))
k = sorted(d.items())
print(dict (k))



# 6. Write a program to extract the words starting with lowercase letter present in the list. [‘Nissan’,
# ‘maruti’, ‘hyundai’, ‘Volkswagen’, ‘audi’]
list1 =['Nissan','maruti', 'hyundai', 'Volkswagen', 'audi']
list2=[]
for i in list1:
    if i[0].lower()==i[0]:
        list2.append(i)
print(list2)

# 7. Write a program using dictionary comprehension which will contain the key value pair of i:i**2. 
# Value of ‘i’ will start from 1 and will go upto 10.
dict={}
for i in range(11):
    dict[i]=i**2

print(dict)

# 8. Take the input marks from user using input() function and find out the grade of the students. Note
# the grading will be in this manner – (100 – 91) – A1, (90-81) – A2, (80-71) – B1, (70-61) – B2, (60-
# 51) – C1 (50-40) – C2 and less than 40 students will ‘Fail’. Also make sure user should input the 
# marks in the range 0<=marks<=100, if user will input some other marks in should print invalid 
# marks.

n=int(input("Enter marks for grade: "))
if n < 40:
    print("fail")
elif n < 50 and n > 40 :
    print("C2")
elif n < 60 and n > 50:
    print("C1")
elif n < 70 and n > 60:
    print("B2")
elif n < 80 and n > 70:
    print("B1")
elif n < 90 and n > 80:
    print("A2")
elif n < 101 and n > 90:
    print("A1")
else:
    print("Invalid")


# 9. Given a list [1,2,1,5,9,10,2,2,7,5,3,10,8,9,15,17,21,16,17,90] find the difference between the 
# length of the list and the count of unique elements in the list.

list_2 =[1,2,1,5,9,10,2,2,7,5,3,10,8,9,15,17,21,16,17,90] 

len_of_list =len(list_2)
count=0
for j in list_2:
    if list_2.count(j)==1:
        count+=1

print(len_of_list-count)


# 10. In the given String -- ‘MsYs TecHNOlogiEs iS a gREat place To woRk’ find the count of 
# lowercase and uppercase letters.

string ="MsYs TecHNOlogiEs iS a gREat place To woRk"
string1=string.replace(" ","")
lower_case_letters= 0 
upper_case_letters=0
for k in string1:
    if k.lower()==k:
        lower_case_letters+=1
        #print(k)
    elif k.upper()==k:
        upper_case_letters+=1
print(lower_case_letters)
print(upper_case_letters)


# 11. Write a python function with name reverse_vowel that takes one string as an argument and 
# reverse the order of vowels present in the string. The function should return the string having 
# reversed order of vowels. For example – If the input string which is given as argument is ‘Hello’ 
# then the output string should be ‘Holle’. You need to reverse the vowel irrespective of lowercase or 
# uppercase.

def reverseVowels(s):
        s = list(s)
        left = 0
        right = len(s) - 1
        m = 'aeiouAEIOU'
        while left < right:
            if s[left] in m and s[right] in m:
                
                s[left], s[right] = s[right], s[left]
                
                left += 1; right -= 1
            
            elif s[left] not in m:
                left += 1
            
            elif s[right] not in m:
                right -= 1
            
        return ''.join(s)

s="Hello Wirlda"
s1=reverseVowels(s)
print(s1)

primes=[]
for i in range(2,11):
    flag=0
    if i < 2:
        continue
    for x in range(2,i):
        if i % x == 0:
            flag=1
            break

    if flag==0:
        primes.append(i)

print(primes)


# 13. Write a lambda function which takes two input arguments x and y. If x is greater than y then it 
# should return square of y and if y is greater than x, then it should return square of x.

x=int(input("Enter num1: "))
y=int(input("Enter num2: "))

num = lambda x,y: x**2 if x>y else y**2
print(num(x,y))

# 14. Given two lists --
# list_1 = [‘Msys’, ‘Tata’, ‘Wells’, ‘Mobinius’]
# list_2 = [‘Technologies’, ‘Power’, ‘Fargo’, ‘Technologies’]
# Write a python code using map and lambda function which will create the list named as my_list 
# consisting of the combination of first name and second name from list_1 and list_2 respectively. 

list_5 = ['Msys', 'Tata', 'Wells', 'Mobinius']
list_6 = ['Technologies', 'Power', 'Fargo', 'Technologies']

list_7 = map(lambda x,y: x+y,list_5,list_6)
print(list(list_7))


# 15. Given a list --
# list_1 = [10, 12, 15, 67, 95, 45, 43, 89, 91, 80, 75, 78, 94, 100]
# use the filter() function to find the list of numbers that are multiple of either 2 or 5.

list_3 = [10, 12, 15, 67, 95, 45, 43, 89, 91, 80, 75, 78, 94, 100]   
list_4 =filter(lambda x : x %2 ==0 or x% 5 ==0,list_3)
print(list(list_4))




m= ["hello","world"]
for i in m:
    print(i[::-1])


# 17. Write a program to replace duplicate adjacent alphabets from a given string with ‘_’. For Example -- input given string : 'abcdaa hssbbye' and output : ‘abcda_ hs_b_ye’
string ='abcdaa hssbbye'
str_=""
for i in range(len(string)-1):
    if(string[i]!=string[i+1]):
        str_=str_+string[i]
        if(string[i]==string[i-1]):
            str_=str_+"_"
    
print(str_)
 
# 18. Print the below rhombus pattern according to the given number
# for eg: given number is 4 then 
# o/p will be 
#    1
#  212
#   	32123
# 	4321234
#   	32123 
#  212 
#    1

# Ans:- 
n = int(input("Enter a number:"))
for i in range(1,n+1):
    print(" " * (n-i),end="")
    for j in range(i,0,-1):
        print(j,end="")
    for k in range(2,i+1):
        print(k,end="")
    print()
for i in range(n-1,0,-1):
    print(" " * (n-i),end="")
    for j in range(i,0,-1):
           print(j,end="")
    for k in range(2,i+1):
           print(k,end="")
    print()
# 19. Write a function which takes input string from the user as argument and the character also taken  by the user as the argument and remove all the occurences of that character from the string. Also if  the given character is not present in the string your function should raise the exception stating that  “Given character is not present in the string. Please try with a new one”.
def remove_char(string, char):
    if char not in string:
        raise ValueError("Given character is not present in the string. Please try with a new one.")
    return string.replace(char, '')
string = input("Enter a string: ")
char = input("Enter a character to remove: ")
try:
	new_string = remove_char(string, char)
	print("New string:", new_string)
except ValueError as e:
	print(e)
#Output:1
# Enter a string: Madhu is doing a task
# Enter a character to remove: task
# New string: Madhu is doing a
 
# #Output:2
# Enter a string: Madhu is doing a task
# Enter a character to remove: sudhan
# Given character is not present in the string. Please try with a new one.
# 20. You are given a string having alphabets,digits,special characters. Write three different functions  to extract the digits[should be in sorted order], special character & vowels[should be in reverse]  from the given string.
# i/p string : "abcd123bye09@8"
# o/p: digits - 012389
#  special character - @
#  vowels - ea
def extract_digits(input_str):
    digits = [char for char in input_str if char.isdigit()]
    digits = sorted(set(digits))
    return ''.join(digits)
 
def extract_special_characters(input_str):
    special_chars = [char for char in input_str if not char.isalnum()]
    return ''.join(special_chars)
 
def extract_vowels(input_str):
    vowels = [char for char in input_str if char.lower() in 'aeiou']
    vowels = vowels[::-1]
    return ''.join(vowels)
input_str = "abcd123bye09@8"
digits = extract_digits(input_str)
special_chars = extract_special_characters(input_str)
vowels = extract_vowels(input_str)
print("Digits:", digits)
print("Special characters:", special_chars)
print("Vowels:", vowels)
#Output:
# Digits: 012389
# Special characters: @
# Vowels: ea
 
# 21. You are given a string and width. Your task is to wrap the string into paragraph of width in  reverse order. Blank spaces should be ignored.
# for eg: i/p - first line contains a string with blank spaces - Hello, welcome to this  organisation.
#  the second line contains the width - 4
#  o/p
# lleH
# ew,o
# mocl
# tote
# osih
# nagr
# tasi
# .noi
string = "Hello, welcome to this organisation."
width = 4
string=string.replace(" ","")
# Reverse the string and remove blank spaces
#string = string[::-1].replace(" ", "")
# print(string)
for i in range(0,len(string),4):
     print(string[i:i+4])

#Output:
# lleH
# ew,o
# mocl
# tote
# osih
# nagr
# tasi
# .noi
# 22. Find the palindrome words with the count value from the given string.Output should be in the form of dict. key will be a palindrome word and value will be number of occurence.
# i/p given a string - Nittin & his mom went to a park last friday. His Mom observed that the weather was too cool. Nittin also met his sis. If we reverse the number 1331 then we also get 1331. 
# o/p - {'nittin': 2, 'mom': 2, 'sis': 1, '1331': 2}
a="Nittin & his mom went to a park last friday. His Mom observed that the weather was too cool. Nittin also met his sis If we reverse the number 1331 then we also get 1331"
b=a.split(" ")
list_=[]
for i in range(len(b)):
    c=(b[i][::-1]).upper()
    d=b[i].upper()
    if (c==d):
    	if(len(d)!=1):
        	list_.append(d)
set_=sorted(list(set(list_)))
dict_={}
for i in set_:
    dict_[i]=(list_.count(i))
print(dict_)
#Output:
{'1331': 2, 'MOM': 2, 'NITTIN': 2, 'SIS': 1}
# 23. create 2 dictionaries as follows:
# dict1 = {'name': 'Msys', 'Place': 'Pune'}
# dict2 = {'EmpID': 0001, 'Salary': 50000}
# Perform following operations:
# a. create single dictionary by merging dict1 & dict2
# b. update the salary to 10%
# c. update age to 35
# d. extract & print all the values & keys separately in tuple.
# e. delete the element with key 'Age' & print the dictionary elements.
dict1 = {"name": "Msys", "Place": "Pune"}
dict2 = {"EmpID": 1, "Salary": 50000}
#way1
dict1.update(dict2)
print(dict1)
print("&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&")
#way2
merge_dict=({**dict1,**dict2})
print(merge_dict)
print("-------------------------------------------------")
#update the salary
present_salary=merge_dict["Salary"]
updates_salary = (present_salary + (present_salary * 0.1))
print(updates_salary)
print("-------------------------------------------------")
#add age:
merge_dict["age"]=35
print(merge_dict)
print("-------------------------------------------------")
#values,keys
print(tuple(merge_dict.keys()))
print(tuple(merge_dict.values()))
print("-------------------------------------------------")
#delete age:
del merge_dict["age"]
print(merge_dict)
#Output:
# {'name': 'Msys', 'Place': 'Pune', 'EmpID': 1, 'Salary': 50000}
# {'name': 'Msys', 'Place': 'Pune', 'EmpID': 1, 'Salary': 50000}
# -------------------------------------------------
# 55000.0
# -------------------------------------------------
# {'name': 'Msys', 'Place': 'Pune', 'EmpID': 1, 'Salary': 50000, 'age': 35}
# -------------------------------------------------
# ('name', 'Place', 'EmpID', 'Salary', 'age')
# ('Msys', 'Pune', 1, 50000, 35)
# -------------------------------------------------
# {'name': 'Msys', 'Place': 'Pune', 'EmpID': 1, 'Salary': 50000}
 
# 24. You have given a string str1 = "abcbaefabcabchijkl"
# your task is to find the combination of given word without repetition, present in the string , given  word 'abc'
# o/p = 7
# explanation :
# abc, cba,
# cba,
# bca, acb
# cab, bac
# Ans:- 

from itertools import permutations
string= "abc"
string_permutations = list(permutations(string))
string_permutations = ["".join(permutations) for permutations in string_permutations]
print(string_permutations)
print(len(string_permutations))

# 25. Given an Integer n, count the total number of times 1 is appearing in all non-negative integers  less than or equal to n.
# Ex – n = 13, output should be 6
# method – 1 is coming 6 times starting from number 0 till 13 in ‘1’, ‘10’, ‘11’, ‘12’, ‘13’. Also note 1 is coming 2 times in 11. That is why 6 is the output

# Ans:-

n = int(input("Enter a number:"))
count = 0
for i in range(n+1):
    if str(1) in str(i):
        count += str(i).count(str(1))
print(count)

 
# 26. Design a binary tree structure in python/any preferred language in such a way that it is in the  form of a triangle and built on AND logic. Initially it looks like the below structure.
# L6 1
# L5 1 1
# L4 1 1 1
# L3 1 1 1 1
# L2 1 1 1 1 1
# L1 1 1 1 1 1 1
# If any value at L1 level is updated then the whole tree should get updated accordingly. For example, if third value at L1 level is updated to 0 then the tree should get updated as below.
# L6 0
# L5 0 0
# L4 0 0 0
# L3 0 0 0 1
# L2 1 0 0 1 1
# L1 1 1 0 1 1 1
# 27. Need to find minimum number of new chair purchase for work area with simulated set of array  values.
# C - A new employee comes to work area and new chair need to purchase
# R - Employee from work area goes to meeting room and free up the chair
# U - Employee comes from meeting room and occupy the chair
# L - Leaves the work area and free up the chair
# Input :
# n = 3
# simulated value : ['CCRLU', 'CRLCUC', 'CCCC']
# Output:
# 2
# 2
# 4
# 28. Given a string s and an integer k, reverse the first k characters for every 2k characters counting from the start of the string.
# If there are fewer than k characters left, reverse all of them. If there are less than 2k but greater  than or equal to k characters, then reverse the first k characters and leave the other as original.
# Input: s = "abcdefg", k = 2
# Output: "bacdfeg"
# Input: s = "abcd", k = 2
# Output: "bacd"  
# Ans:- 
s="abcdefg"
k=2 
m=s[:k]
m1=m[::-1]
n=m1+s[k:]
print(n)
