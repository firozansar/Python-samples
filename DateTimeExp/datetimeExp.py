#!/usr/bin/env python3
from datetime import date
from datetime import datetime

## DATETIME OBJECTS
# Get today's date from the datetime class
now = datetime.now()
print  ("The current date and time is {0}".format(now))

current_year = now.year
current_month = now.month
current_day = now.day

print (current_month)
print(f'Today\'s date is {current_day}/{current_month}/{current_year}.')

# Get the current time
t = datetime.time(datetime.now())
print ("The current time is {0}".format(t))

## DATE OBJECTS
# Get today's date from the simple today() method from the date class
today = date.today()
print ("Today's date is {0}".format(today))

# print out the date's individual components
print ("Date Components: {0}, {1}, {2}".format(today.day, today.month, today.year))

# retrieve today's weekday (0=Monday, 6=Sunday)
print ("Today's Weekday #: {0}".format(today.weekday()))

# weekday returns 0 (monday) through 6 (sunday)
wd = date.weekday(today)  
# Days start at 0 for Monday 
days = ["monday","tuesday","wednesday","thursday","friday","saturday","sunday"]
print ("Today is day number {0}".format(wd))
print ("Which is a {0}".format(days[wd]))