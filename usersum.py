# this program prints sum of numbers
# eg :- if user enter 8 it will do 8+7+6+5+4+3+2+1  and return sum

sum_of_numbers = 0
nums = int(input("enter the number "))
if nums == 0:
    print("we can't sum with zero numbers")
else:
    for i in range(nums, 0, -1):
        sum_of_numbers += i
print(sum_of_numbers)


# sum_of_numbers = 0
# while True:
#     nums = int(input("enter the number "))
#     if nums == 0:
#         break
#     else:
#         for i in range(1, nums+1):
#             sum_of_numbers += i
# print(sum_of_numbers)


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


