x=7
a=eval("x**2")
print(type(a))


def add(c,k):
    c.test=c.test+1
    k=k+1
class A:
    def __init__(self):
        self.test = 0
def main():
    Count=A()
    k=0
 
    for i in range(0,25):
        add(Count,k)
    print("Count.test=", Count.test)
    print("k =", k)
main()


s= "MSys&Technologies@chennai*"
s1=""
for i in s:
    
    if i.isalpha():
        s1+=i
    else:
        s1+=" "
print(s1) 


# s1={3,4,5}
# s={1,2,3}
# s2=s+s1
# num="1432219"
# for i in range(len(num)):
#     for j in range(i,len(num),3):
#         print(num[j:])

# def a():
#     s=123
#     print(s)



s = list("adfew$vf&yviy*ugv%y")

n1,n2=0,len(s)-1
m="aeiou"
while n1<n2:
    if s[n1] not in m:
        n1+=1
    elif s[n2] not in m:
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

num1= 2 
num2=5 
result = 0
for i in range(1,num2+1):
    num1 += i 
print(num1)