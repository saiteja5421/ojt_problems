from addsub import *
from muldiv import *



def main():
    print(add(1,2))
    print(sub(2,1))
    print(__name__)
    

if __name__=="__main__":
    main()




# a=("username",)
# b=list(a)
# b.append("password1")
# print(tuple(b))

# try:
#     print("msys"+2007)
# except:
#     print("Error: Cannot concatentate str and int")




d={"priya":{"location":"Hyderbad","joiningDate":"05/09/2022"}}
for i,j in d.items():
    for k,l in j.items():
        if l == "Hyderbad" :
            pass 
        else:
            print(list(map(int,l.split("/"))))

            
            

