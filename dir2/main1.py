
# l =[1,2,3,4,5,6,7,8,9,10]
# list1=[]

# for i in l:
#     if i % 2 != 0:
#         list1.append(i)

# print(list1)

# list1 = [1,2,34,4,5]
# list2 = list(filter(lambda x: x%2 == 0,list1))
# print(list2)



# list3 = [10,20,30,40,50,60,70]
# n=4
# x=len(list3)
# new_list=[]
# new_list=list3[x-n:]
# new_list.extend(list3[:x-n])
# print(new_list) 


# l = [1,2,3,2,4,5,2,4,2,7,8,5,6,8,10]
# dict={}
# for i in l:
#     if i % 2 == 0:
#         dict[i]=l.count(i)
# print(dict)

# import time
# while True:
#     actual_time = int(time.time())
#     #print(actual_time)
#     for i in range(5,0,-1):
#         print("*"*i)
#     waiting_time = actual_time + 10
#     while True:
#        	if int(time.time()) == waiting_time:
#            	break





a = "abb24ccc8ddbbca1"
x= ''

for i in a:
    if i.isalpha() and (i not in x) :
        x+=i+str(a.count(i)) 
    elif i.isdigit():
        x+=i

print(x)














                