#Write a program to display current date and time using datetime module.
from datetime import datetime

now = datetime.now()
datetime = now.strftime("%Y-%m-%d %H:%M:%S")
print("Current Date and Time:",datetime)
print("Current Year : ",now.year)
print("Current Month : ",now.month)
print("Current Date : ",now.day)
print("Current Hour : ",now.hour)
print("Current Minute : ",now.minute)
print("Current Second : ",now.second)
