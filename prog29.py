import re

text = "Python, Java, C, Python"
print(text)
match_result = re.match("Python", text)
search_result = re.search("Java", text)
findall_result = re.findall("Python", text)

if match_result:
    print("match:", match_result.group())
else:
    print("match: Pattern not found")

if search_result:
    print("search:", search_result.group())
else:
    print("search: Pattern not found")

print("findall:", findall_result)
