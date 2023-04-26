def sort_list(list2):
    temp=0 
    for i in range(0,len(list2)):
        for j in range(0,len(list2)):
            if list2[i] > list2[j]:
                temp=list2[i]
                list2[i]=list2[j]
                list2[j]=temp 

    return list2 

print(sort_list([2,6,-1,0,3,-4]))
        

def palindrome_strings(a):
    if a == a[::-1]:
        return a
    
print(palindrome_strings("mam"))


def even_odd(l):
    odd=[]
    even=[]
    for i in l:
        if i % 2 == 0:
            even.append(i)
        else:
            odd.append(i)
    d={}
    d["even"]=even
    d["odd"]=odd 

    return d 

print(even_odd([1,2,3,4,5,6,7,8,9,10])) 

print(["user1","user2"]+["user3"])

username="Msys"
department="QA"

email="{}.{}@gmail.com".format(username,department)
print(email)


s= "MSys&Technologies@chennai*"
s1=""
for i in s:
    if i.isalpha():
        s1+=i
    else:
        s1+=" "
print(s1) 


d={
    "departement":["Bakkt","cisco"],
    "Team":["Red","Black","Yellow"]
 }

output= [
    { "departement":"Bakkt","Team":"Red"},
    {"departement":"Bakkt","Team":'Black'},
    {"departement":"Bakkt","Team":'Yellow'},
    {"departement":"cicso","Team":'Red'},
    {"departement":"cicso","Team":'Black'},
    {"departement":"cicso","Team":'yellow'},

]
u=[]
for j in d["departement"]:
    for k in d["Team"]:
        u.append({"departemt":j,"Team":k})
print(u)


#indexError  
l1=[1,2,3]
try:
    s=l1[3]
except IndexError as e:
    print("index Error")

try:
    s1=23+'5'
    print(s1)
except TypeError as a:
    print(a)


try:
    class vehical():
        def __init__(self) -> None:
            pass
    m=vehical()
    m.add()
except AttributeError :
    print("class has no attribute")

def genator_func():
    
    for i in range(1,25):
        if i % 2 ==0 and i % 5 ==0 :
            yield i 

s= genator_func()
for i in s:
    print(i,end=" ")

print()
for i in range(1,6):
    if i % 2 != 0:
        l=""
        for i in range(1,i+1):
            l+=str(i) 
        print("*"+l)
    else:
        l1=""
        for i in range(i,0,-1):
            l1+=str(i)
        print(l1+"*")


n1="1231"
n2="1"

l1=["a","b"] 
l2=[1,2]

data={l1[i]:l2[i] for i in range(len(l1))}
print(data)

data=dict(zip(l1,l2))
print(data)

from functools import reduce 

sum_=reduce(lambda x,y:x+y,l2)
print(sum_)


def only_list_arguments(a):
    try:
    #print(type(a))
        if type(a) != list:
            raise "its not a list"
        else:
            print(a)
    except:
        print("this function accepts only list arguments")
    
# import json 
# with open("Sample.json","r")  as p:
#     p1=p.read()
#     print(type(p1))
#     y=json.loads(p1)
#     print(type(y))
# only_list_arguments(123)

import random
import string
def random_password(l):
    password=""
    for i in range(int(l/2)):        
        a=random.choice(string.ascii_letters)
        b=random.choice([1,2,3,4,5,6,7,8,9]) 
        password+=a+str(b)

    print(password)
    
random_password(4)

def generatorss(l):
    for i in range(1,l+1):
        if i % 5 ==0 and i % 2==0:
            yield i

b=generatorss(50)
for i in b:
    print(i)


# import time
# def time_taken():
#     start=time.time()
#     time.sleep(5)
#     end=time.time()
#     print(end-start)

# time_taken()


li=[7,8,2,3,6,9,2,8]
target=14 

def two_sum(li):
    for i in range(1,len(li)):
        a=li[0]
        b=li[i]
        if (a+b)==target:
            return [a,b]
    return two_sum(li[1:])
c,d=two_sum(li)
print(li.index(c),li.index(d))



# result=[[number1 for div in range(2,10) if number1 % div ==0] for number1 in range(1,1001)]
# print(result)


n=3
print(" "*(n+1)+"*")
for i in range(n*2):
    if i % 2 !=0:
        print(" "*(n-int(i/2))+"*"+"_"*(i)+"*")


string="aaadaa"
sub_string="aa"

count=0
for i in range(count,len(string)):
    if string[count:i+len(sub_string)]==sub_string:
        print(count,i+len(sub_string)-1)
    count+=1


text="Be Happy".split(" ")
#t=text.split(" ")
d={}
for i in text:
    d[i]=len(i)
print(d)

def function_arg(*args,**kwargs):
    print(type(kwargs))
    print(type(args))
function_arg(3,4,a=1,b=2)

a="abcdef"
b=""
for i in range(len(a)):
    b+=a[i]+str(i+1)
print(b)

# l=[i  for i in range(51) if i %2==0 if i % 5 ==0]
# print(l)


# n=6
# def patteren(n):
#     print(" "*n+"*")
#     count=1
#     for i in range(1,n):
#         print(" "*(n-i)+"*"+"_"*count+"*")
#         count+=2
# patteren(n)
import re
s="Saiteja@3"
def strong_password(s):
    if re.search(r'[a-z]',s) and \
        re.search(r"[A-Z]",s) and \
              re.search(r"\d",s) and \
                  re.search(r"[!@#$%^&*()]",s):
                    return True
    return False

print(strong_password(s))

import inspect
def test(*args,**kwargs):
    pass
test(1,name="sai")
print(inspect.getfullargspec(test))


for i in range(1,4+1):
    s=""
    for j in range(i):
        s+=str(i)
    print(" "*(4-i-1)+s)
