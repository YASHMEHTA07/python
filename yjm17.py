#Write a program to demonstrate list dictionary and set comprehensions


lst1=[i**2 for i in range(1,11)]
print("SQUARE FOR 1 TO 10 IS  ",lst1)

dic={"STATE": 'GUJARAT', "CITY": "RAJKOT", "UNIVERSITY": "MARWADI"}

dic = {key: value for key, value in zip(dic.keys(), dic.values())}

print("DICTINORY COMPREHENSIONS :- ", dic)

set1={i*2 for i in range(1,11)}
print("USING SET ",set1)
