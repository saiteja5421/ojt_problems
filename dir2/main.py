nput= [1,2,3,2,4,2,4,7,8,4,5,8,6,9,2]
dict_even = {}
for i in nput:
    if i % 2 == 0:
        dict_even[i]=nput.count(i)
print(dict_even) 

dict = {"name" : "saiteja","roolno" : 3098,"comapany": "MSys"}
dict1={}
for key in sorted(dict):
    dict1[key]=dict[key] 

print(dict1)

    


#using loop 
Sample_input= [10,20,30,40,50,60]
n = 3 
output= []
for i in range(len(Sample_input)-n,len(Sample_input)):
    output.append(Sample_input[i])
for i in range(0,len(Sample_input)-n):
    output.append(Sample_input[i])
print(output) 

#using indexing
output2 = []
output2=Sample_input[len(Sample_input)-n:]
output2.extend(Sample_input[:len(Sample_input)-n])
print(output2)

match = "version"
input="Upgraded_image_version_8.0.4.3"
if match in input:
    print('YES')
else:
    print('NO')

#swap_element  
# def Swap_elemts(num,s,a):
#     temp=num[s]
#     num[s]=num[a]
#     num[a]=temp 
# first_arg = int(input("Enter first position to swap: "))
# second_arg = int(input("Enter second position to swap: "))
# num = [1,2,3,4,5,6,7]
# Swap_elemts(num,first_arg,second_arg)
# print(num)

match ="verasion"
input = str(8) 
print(match+input)

#monkeypatching 

def hello(self):
    print("hello() function calling")

def monkey():
    print("monkey() function is calling")

hello = monkey
hello()



#int("hello")
# l = [1,2,3,4]
# a,b,c =l 
# import math
# math.sqrt(-10)

num1= 2 
num2=5 
result = 0
for i in range(1,num1+1):
    result += num2 
print(result)


def transform_string(input_str):
    output_str = ""
    current_count = 0
    index=0
    while index<len(input_str):
        if not input_str[index].isdigit():
            temp=index
            while temp<len(input_str):
                if input_str[index]==input_str[temp]:
                    current_count+=1
                    temp+=1
                else:
                    break 
            output_str+=input_str[index]+str(current_count)
            current_count=0
            index=temp
        else:
            output_str+=input_str[index]
            index+=1
    
    # add the last character and its count to the output string
    #output_str += current_char + str(current_count)
    
    return output_str

s = transform_string("abbbc123adbddd")
print(s)



names_list = ['Prabhu', 'Rahul', 'Arunesh', 'Sonali', 'Rakshit']
sorted_name = sorted(names_list,key=lambda x : x[-1])
print(sorted_name)



# code for testing decorator chaining
def decor1(func):
	def inner():
		x = func()
		return x * x
	return inner

def decor(func):
	def inner():
		x = func()
		return 2 * x
	return inner

def decor2(func):
    def inner():
        x=func()
        return x + 1
    return

@decor1
@decor
def num():
	return 10

@decor
@decor2
def num2():
	return 10

print(num())
print(num2())