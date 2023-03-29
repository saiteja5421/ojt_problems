
def validparenthese(n):
    a=[]
    for i in n:
        if i in "({[":
            a.append(i)
        elif i == ")" :
            if len(a)==0 or a[len(a)-1] != ")":
                return False
            else:
                a=a[:len(a)-1]
                break
        elif i == "}" :
            if len(a)==0 or a[len(a)-1] != "}":
                return False
            else:
                a=a[:len(a)-1]
        elif i == "]" :
            if len(a)==0 or a[len(a)-1] != "}":
                return False
            else:
                a=a[:len(a)-1]
    return len(a) == 0



n= "(){}[]"

b =validparenthese(n)
print(b)
