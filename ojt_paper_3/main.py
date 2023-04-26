# 1. Write a program in which two strings are given and determine if they share a
# common substring. A substring may be as small as one character. The function
# returns either “YES” or “NO”.
def common_substring(str1,str2):
    for i in str1:
        if i in str2:
            return True 
    return False
    
a=common_substring("Hello","World")
print(a)

# 2. Write a decorator function that will record the number of times a function is
# called. Your decorator function should be called record_calls and call_count
# attribute that keeps track of the number of times it was called.
def record_calls(func):
    call_count = 0
    for i in range(5):
        func()
        call_count+=1
    print(call_count)

@record_calls
def one_to_ten():
    print("Hello")

# obj = record_calls(one_to_ten)
# print(obj)

l1=[0,2,4,6,8]
l2=[1,3,5,7,9]
l3=[]
def two_list(l1,l2):
    for i in range(len(l1)):
        l3.append(l1[i])
        l3.append(l2[i])
    print(l3)

two_list(l1,l2)

# 4. Write to_celsius function that accepts a temperature in Fahrenheit as input and
# returns a temperature in Celsius. 

def to_celsius(f):
    c=(f-32)* 5/9 
    return c 

print(to_celsius(98.6))




# print(str(int(1/3 * 100))+"%") 
# 5. Write a function that accepts an iterable and returns a new iterable with all items
# from the original iterable except for duplicates.
# Ex. uniques_only([1, 2, 2, 1, 1, 3, 2, 1])
# [1, 2, 3]

def uniques_only(list1):
    list2=[]
    for i in list1:
        if i not in list2:
            list2.append(i)
    return list2 

uniques=uniques_only([1, 2, 2, 1, 1, 3, 2, 1])
print(uniques)


# 6.Write a function to_percent which accepts a number representing a ratio and
# returns a string representing the percentage representation of the number to one
# decimal place.


def to_percent(n):
    a,b = n.split(":")
    percent = int(a)/int(b)*100 
    return "{}%".format(round(percent,1))
n = "5:13" 
g= to_percent(n)
print(g)

# 7. Write a function that accepts two strings and returns True if the two strings are
# anagrams of each other.

def string_anagram(a,b):
    if len(a) != len(b):
        return False 
    elif sorted(a.lower()) == sorted(b.lower()):
        return True 
    else:
        return False
    
anagram = string_anagram("Hello","llohe")
print(anagram)

# 8. Write Row class that accepts any keyword arguments given to it and stores these
# arguments as attributes.
# Ex. >>> row = Row(a=1, b=2)
# >>> row.a
# 1
# >>> row.b
# 2 

class Row():
    def __init__(self,a,b):
        self.a=a 
        self.b=b 

row=Row(1,2)
print(row.a)
print(row.b)
l=[1,2,3,4]
def split_list(l):
    l1=[]
    l1.append(l[:int(len(l)/2)])
    l1.append(l[int(len(l)/2):])
    return l1 

print(split_list(l))


def last_items(l,n):
    l2=[]
    for i in range(n,0,-1):
        l2.append(l[-i])
    return l2
print(last_items([1,2,3,4,5,6],3))

# 9. Create a function is_leap_year that accepts a year and returns True if (and only
# if) the given year is a leap year.

def leap_year(year):
    if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
        return "{} is a leap year".format(year)
    else:
        return "{} is not a leap year".format(year)

leap_year_obj = leap_year(2017)
print(leap_year_obj) 

# 10. Write a function combine_lists should take two lists and return a new list
# containing all elements from both lists.

def combine_lists(list1,list2):
    list3= []
    list3.extend(list1)
    list3.extend(list2)
    return list3 

l1=[1,2,34,4]
l2=[6,7,8,9]
f = combine_lists(l1,l2)
print(f)

# 11. Write a function, last_lines, which returns lines in a given ASCII text file in
# reverse order.
# For example, given the following file, my_file.txt:
# This is a file
# This is line 2
# And this is line 3
# The last_lines function should work like this:
# >>> for line in last_lines('my_file.txt'):
# ... print(line, end='')
# ...
# And this is line 3
# This is line 2
# This is a file

# with open("ojt_paper_3/my_file.txt","r") as file:
#     s=file.readlines()[::-1]
#     for i in s:
#         print(i,end="")

# 12. Write a function called parse_ranges, which accepts a string containing ranges of
# numbers and returns an iterable of those numbers.
# Ex: >>> parse_ranges('1-2,4-4,8-13')
# [1, 2, 4, 8, 9, 10, 11, 12, 13]

def parse_ranges(a):
    list3=[]
    for i in a:
        # print(i[0],i[2])
        d,f = i.split("-")
        # print(d,f)
        for j in range(int(d),int(f)+1):
            list3.append(j)
    return list3

c = parse_ranges(('1-2','4-4','8-13'))
print(c)

# 13. Write a function that accepts a string containing lines of numbers and returns a
# list of lists of numbers.
# Ex. matrix_from_string("3 4 5")
# [[3.0, 4.0, 5.0]]

def string_list(s):
    list5=[]
    for i in s.replace(" ",""):
        list5.append(float(i))
    print([list5]) 

string_list("3 4 5")

def get_hypotenuse(a,b):
    c=(a**2+b**2)*0.5
    return c 

print(get_hypotenuse(3,4))



# Write a function that takes two strings representing dates and returns the string
# that represents the earliest point in time ? Ex. get_earliest("01/27/1832",
# "01/27/1756") return '01/27/1756'

def earliest_day(date1,date2):
    d1,m1,y1=date1.split("/")
    d2,m2,y2=date2.split("/")
    if y1< y2:
        return date1 
    elif y1 > y2 :
        return date2 
    if m1 < m2:
        return date1 
    elif m1 > m2:
        return date2 
    if d1 < d2:
        return date1 
    elif d1> d2:
        return date2 
    
print(earliest_day("01/27/1832","01/27/1756"))


def float_range(start,stop,step):
    l=[]
    while start<stop:
        l.append(start)
        start+=step 

    return l

# r=float_range(0.5,2.5,0.5)
# # for i in r:
# #     print(i)
        








# def floating_range(start,stop,step):
#     list1=[]
#     for i in range(start,stop,step):
#         list1.append(i)
#     print(list1)

# floating_range(0.5,2.5,0.5)

def iterator_func(obj):
    return hasattr(obj,'__next__')
print(iterator_func([1,2]))

def int_to_roman(num):
    """
    Converts an integer to a Roman numeral.
    """
    # Define the Roman numeral symbols and their values
    roman_symbols = {
        1000:'M',
        900: 'CM',
        500: 'D',
        400: 'CD',
        100: 'C',
        90: 'XC',
        50: 'L',
        40: 'XL',
        10: 'X',
        9: 'IX',
        5: 'V',
        4: 'IV',
        1: 'I'
    }
    
    # Initialize an empty string to hold the Roman numeral
    roman_numeral = ''
    
    # Iterate through the Roman numeral symbols in descending order of value
    for value, symbol in roman_symbols.items():
        # Repeat the symbol as many times as necessary
        while num >= value:
            roman_numeral += symbol
            num -= value
    return roman_numeral

a= int_to_roman(15)
print(a)



# 1. Find the largest number which you can make by only removing one instance of given number from the input number 

# Input : test_list = [2323, 82, 129388, 95]

test_list = [2323,82,129388,95] 

def list_dict(list1):
    dict={}
    for i in list1:
        i=str(i)
        key,value=i[:int(len(i)/2)],i[int(len(i)/2):]
        dict[int(key)]=int(value) 
    print(dict)
list_dict(test_list)


# def meetup_date(date,time):
#     pass 
# import contextlib 
# @contextlib.contentmanager
# def suppress():
#     pass



# s= [[j for j in range(i)] for i in range(2,10)]
# print(s)

import datetime 

def meetup_date(year,month,day):
    obj=datetime.datetime(year,month,day)
    print(obj)

meetup_date(2012,3,22)


def Invalid(Expection):
    pass

# import os 
# print(os.cpu_count())




