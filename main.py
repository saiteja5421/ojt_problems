#   Count the number of characters in a string and stored result ij dictionary
#    ex: input : "google.com"  , output : {'g': 2, 'o': 3, 'l': 1, 'e': 1, '.': 1, 'c': 1, 'm': 1}
def lettercount(word):
    letter_dict = {}
    for i in word:
        # dict[i]=a.count(i)
        count = 0
        special_list = [" ", ".", "@", "#", "!", "$", "&", "*","%"]
        if i in special_list:
            continue
        # if i == "." or i == " " or i == "@" or i == "#" or i == "!":
        #     continue
        else:
            for j in word:
                if i == j:
                    count = count + 1
        letter_dict[i] = count
    return letter_dict


string = input("Enter the Word to count ")

print(lettercount(string))

# program to calculate the sum of numbers until the user enters zero
# a = 1
# sum_of_numbers = 0
# print("this program return sum of numbers until you enter zero")
# while a != 0:
#     nums = int(input("enter the number "))
#     if nums == 0:
#         a = 0
#     else:
#         sum_of_numbers = sum_of_numbers + nums
# print(sum_of_numbers)


#monkey patching
def monkey():
    def monkeyFunc(self):
        print("my function")
        
def patchFunc():
    print("patching on monkey")
    
#normal class method call

monkey()
#calling class method after monkey patch
monkey.monkeyFunc=patchFunc
monkey()


#
# #  program to check if a number is armstrong or not
# def armstrong_number(num):
#     l = []
#     for j in str(num):
#         l.append(j)
#     count = 0
#     for i in l:
#         count += int(i) ** 3
#     if count == num:
#         return "its a armstrong number"
#     else:
#         return "its not a armstrong number"
#
#
# c = armstrong_number(153)
# print(c)

#   Write a program to perform all operations as calculator
