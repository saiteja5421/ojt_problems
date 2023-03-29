def sort_list(list2):
    temp=0 
    for i in range(0,len(list2)):
        for j in range(0,len(list2)):
            if list2[i] < list2[j]:
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
    if i.isalnum():
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
        for i in range(1,i+1):
            l1+=str(i)
        print(l1+"*")


n1="1231"
n2="1"


