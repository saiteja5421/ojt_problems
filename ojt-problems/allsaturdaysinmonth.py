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
items =["example (.com)", "MSys", "github (.com)", "keka (.com)"]
for item in items:
    print(re.sub(r"\(.+\)", "", item))
    

str='''
<html>
<body>
<p>This is a paragraph.</p>
</body>
</html>'''
s=re.findall(r"(<[a-z]{4,}>)",str)
print(s)

