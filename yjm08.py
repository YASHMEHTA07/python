#Write a program to explain mutable and immutable objects in Python.

x = 10
print("Original x:", x, "| id:", id(x))
x += 5
print("After x += 5:", x, "| id:", id(x))

my_list = [1, 2, 3]
print("Original list:", my_list, "| id:", id(my_list))
my_list.append(4)
print("After append(4):", my_list, "| id:", id(my_list))

my_tuple = (1, [2, 3], 4)
print("Original tuple:", my_tuple, "| id:", id(my_tuple))
my_tuple[1].append(5)
print("After modifying list inside tuple:", my_tuple)
