list1=["A","B",3,"D","E"]
string="ABCD"
dics={"Student" : "Yash","age":21,"country":"India"}

print("Your List as Follows:- ")
for i in list1:
    print(i)
print(" ")
      
print("Your String as Follow:- ")
for i in string:
     print(i)

print(" ")

print("your dictionary as follows:- ")
for key,value in dics.items():
      print(f"{key}:{value}")
