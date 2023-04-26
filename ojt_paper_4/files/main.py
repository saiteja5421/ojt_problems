import os 

f=input("Enter files with extension with spaces").split()
print(f)

f1="\TxT"
for i in f:
    if ".txt" in i:
        f2=open("D:\Documents\ojt_problems\ojt_problems\ojt_paper_4\TXT\\"+i,"w")
        print(f2)
    elif ".csv" in i:
        f3=open("D:\Documents\ojt_problems\ojt_problems\ojt_paper_4\CSV\\"+i,"w")
        print(f3)



# f1=open("file1.txt","w")
# print(f1)







