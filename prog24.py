#Write a program to generate random numbers using random module.

import random

print("Random Number : - ",random.random())
print("Random Int Number : -",random.randint(1,100))
print("Random Uniform Number  : ",random.uniform(2.5, 10.0)) 
list1 = [16, 28, 13, 54, 65, 86]
print("Random Choice No from The List : - ",random.choice(list1))
