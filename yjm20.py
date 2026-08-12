#Write a program to generate a sequence of numbers using generator functions and yield keyword.

def number_sequence(n):
    for i in range(n,0,-1):
        yield i

n=int(input("enter a positive number: "))

print("generated sequence")
for num in number_sequence(n):
    print(" ",num)

