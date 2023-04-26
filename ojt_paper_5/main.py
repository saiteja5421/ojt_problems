def second_largets():
    l= [1,2,6,3,8,5]
    n=0
    for i in l:
        if i> n:
            n=i
    l.remove(n)
    print(l)
    n1=0
    for i in l:
        if i> n1:
            n1=i 
    print(n1) 
    # for i in range(len(l)):
    #     for j in range(len(l)):
    #         if l[i] < l[j]:
    #             temp=l[i]
    #             l[i]=l[j]
    #             l[j]=temp
    # print(l)

second_largets()

#approach 2 
l1=[1,2,6,3,8,5]
l1=sorted(l1)
print(l1[-2])


def remove_dupli(list1):
    list2=[]
    for i in list1:
        if i not in list2:
            list2.append(i)
    return list2 

print(remove_dupli([1,2,2,2,3,4,5,4,3,2])) 



list3=[1,2,3,4,5,6]
def remove_index_element(list3,idx):
    list3.pop(idx)
    return list3 

print(remove_index_element(list3,2))


list3=list3[len(list3)-2:]+list3[:len(list3)-2]
print(list3)


def prime_numbers_list(l):
    list4=[]
    for i in range(1,11):
        if i > 1:
            for j in range(2,i):
                if i % j ==0:
                    break 
            else:
                #print(i)
                list4.append(i**2)
    print(list4)
    for k in list4:
        #print(l)
        if k in l:
            print(k)

prime_numbers_list([1, 4, 6, 11,15, 24, 19, 25, 27, 30,17])


# f=open("text1.txt","r")
# fl=f.readlines()
# f2=f.readlines()[::-1]
# for i in f2:
#     if "\n" in i:
#         a=i.replace("\n","")
#         print(a)
#     else:
#         print(i)
# sum_of_digits = 0
# f=open("text1.txt","r")
# f=f.readlines()
# for i in f:
#     l=""
#     for j in i:
#         if j.isdigit():
#             l+=j
#     sum_of_digits+=int(l)
# print(sum_of_digits)
    


s = list("adfw$vf&yvy*ugv%uy")

n1,n2=0,len(s)-1
while n1<n2:
    if not s[n1].isalnum():
        n1+=1
    elif not s[n2].isalnum():
        n2-=1
    else:
        temp=s[n1]
        s[n1]=s[n2]
        s[n2]=temp
        n1+=1
        n2-=1
print("adfw$vf&yvy*ugv%uy")
x="".join(s)
print(x)



s1= "I need to work very hard to learn more about algorithms in Python!"
sentence=s1.split()
s=sum(map(len,sentence))/len(sentence)
print(s)

l=[1,2,3,4,5]
from functools import reduce 

# a=reduce()
# print(a)

lst = ['data','science','artificial', 'intelligence'] 
dct = {'data': 5, 'science': 3, 'machine':1, 'learning': 8} 
dct1={}
for i in lst:
    if i in dct.keys():
        dct1[i]=dct[i]
    else:
        dct1[i]=len(i)
print(dct1)

# import pickle 
# sai={"name":"saiteja","rollNo":123}
# db={}
# db["sai"]=sai
# f3=open("pickle.txt","ab")
# pickle.dumps(db,f3)
# f3.close()



def tarnform_string(l):
    string=""
    index=0
    count=0
    while index<len(l):
        if not l[index].isdigit():
            temp=index
            while temp < len(l):
                if l[temp]==l[index]:
                    
                    count+=1
                    temp+=1
                else:
                    break 
            string+=l[index]+str(count)
            count=0 
            index=temp
        else:
            string+=l[index]
            index+=1
    return string
print(tarnform_string("bbbc123adbddd12"))






try:
    first_number=int(input("Enter a number to divid: "))
    second_number=int(input("Enter a number to divid2: "))
    max_number=max(first_number,second_number)
    min_number=min(first_number,second_number)
    if min_number==0:
        raise ZeroDivisionError
    else:
        print(max_number/min_number)
except ValueError as e:
    print("ValueError: {}".format(e))
except ZeroDivisionError :
    print("cannot divide with Zero")


l=[1,None,None,3,None,4]

for i in range(len(l)):
    if l[i]==None:
        l[i]=l[i-1]
print(l)


def Teams(wins,draw,losses):
    points=(wins*3)+(draw*1)+losses*-1

    return points

team1=Teams(3,4,2)
team2=Teams(5,0,2)
team3=Teams(0,0,1)
print(team1,team2,team3)

max_score=max(team1,team2,team3)
print(max_score)

if max_score == team1:
    print("Team1 Wins")
elif max_score == team2:
    print("Team2 Wins")
else:
    print("Team3 Wins")



date,time="2020-01-15 09:03:32.744178".split(" ")
date=date.split("-")
print("Year : {} \nMonth: {} \nday : {}".format(date[0],date[1],date[2]))
print("time: ".format(time))



import contextlib 

@contextlib.contextmanager 
def context():
    print("welcome!")
    yield
    print("End of program")

with context():
    team1=Teams(3,4,2)
    print(team1)
    print("its running in the context manager")

l=[]
for i in range(2,1000):
    div=False
    for j in range(2,10):
        if i % j == 0:
            break
        else:
            div=True
    if div:
        l.append(i)
print(l)



# import inspect 

# def func(a,b):
#     return a**b

# print(inspect.signature(func))





card_num=str(546286074524628)

l=len(card_num)
s="*"*(l-4)
for i in range(4,0,-1):
    s+=str(card_num[-i])
print(s)



a=[8,9,"f",4,5,"g",4]
for i in range(len(a)):
    if type(a[i]) == int:
        a[i]=a[i]*a[i]
    elif type(a[i])== str:
        a[i]=a[i]+a[i]

print(a)

import pickle 
omar={"name":"saiteja","rollno":1029}
d={}
d["Omkar"]=omar 
fil= open("text1.txt","ab")
pickle.dump(d,fil)
fil.close()
fil2=open("text1.txt","rb")
db=pickle.load(fil2)
print(db)
# d2=pickle.loads(d1)
# print(d2)

