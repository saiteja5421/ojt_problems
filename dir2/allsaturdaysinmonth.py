# import calendar 
# from datetime import date
# Year = int(input("enter the year "))
# b = int(input("enter the month "))

# def allsaturdays(Year,b):
#     A=calendar.TextCalendar()
#     for k in A.itermonthdays(Year,b):
#             if k!=0:
#                 day=date(Year,b,k)
#                 if day.weekday()==5:
#                     print("{},{}-{}-{}".format(calendar.day_name[5] ,k,b,Year))

# allsaturdays(Year,b)

import re
items = ames_list =  ["example (.com)", "MSys", "github (.com)", "keka (.com)"]
for item in items:
    print(re.sub(r"\(.+\)", "", item))

str='''<video></video>
jhdfnkjjef <param>
<h1> </h1>'''
s=re.findall(r"<([a-z]{5,})>",str)
print(s)