py =int(input("Enter your python marks: "))
java =int(input("Enter your java marks: "))
c =int(input("Enter your c marks: "))

total_mark=py+java+c
percentage=(total_mark/3)

if percentage<35:
    print("Better Luck Next Time")

elif 35<=percentage<=50:
    print("Pass");

elif 51<=percentage<=60:
    print("Second class");

elif 61<=percentage<=70:
    print("Pass");

else:
    print("First Distinction clas")

