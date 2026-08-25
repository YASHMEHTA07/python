import re

text = "Name: Bobby, Age: 21, Email: bobby@example.com, Phone: 9876543210"

name = re.search(r"Name: ([A-Za-z]+)", text)
age = re.search(r"Age: (\d+)", text)
email = re.search(r"[\w.-]+@[\w.-]+\.\w+", text)
phone = re.search(r"\d{10}", text)

print("Name:", name.group(1))
print("Age:", age.group(1))
print("Email:", email.group())
print("Phone:", phone.group())