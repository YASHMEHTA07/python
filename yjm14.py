num=int(input("Enter a number: "))
total=0
while num:
    total +=num%10
    num//=10

print("Total SUM is:- ",total)
