#Write a program to illustrate variable scope using local global and nonlocal variables

x = "global"

def outer():
    x = "outer local"
    def inner():
        nonlocal x
        x = "this is nonlocal"
        print("inner:", x)
    inner()
    print("outer:", x)

def global_f():
    global x
    x = "changed the value global"
    print("global_f:", x)

print("before:", x)
outer()
print("after outer:", x)
global_f()
print("after global_f:", x)
