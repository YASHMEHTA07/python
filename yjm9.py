#Write a program to define and use user-defined functions with different types of arguments.

def display():
    print("This is simple Display function")

def dis(nm):
    print(f"i  am {nm},This is Positional argument")

def dis1(num=5,sq=2):
    return num**sq;

def keyword_arg(first,last):
    print()
    print("This is keyword argument")
    print(f"Hii My NAME is {first}{last}")

def vari_arg(num,*nm):
    for i in nm:
        print(" ",i*i)

display()

sqr=dis1(num=5,sq=2)
print()

print("This is default argument===",sqr)
print()

keyword_arg(first="bca1",last="A")
print()

dis(nm="yash")
print()

vari_arg(1,2,3,4,5,6,7,8,9)
