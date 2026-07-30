numbers = [10, 20, 30, 40, 50, 60]
print("Original list:", numbers)


print("First element (index 0):", numbers[0])
print("Last element (index -1):", numbers[-1])

print("First three elements:", numbers[0:3])   
print("Elements from index 2 to end:", numbers[2:])
print("Every second element:", numbers[::2])
print("slicing oprator:",numbers[1:4])


numbers[1] = 25
print("After modifying second element:", numbers)


squares = [x**2 for x in numbers]
print("Squares of numbers:", squares)

even_numbers = [x for x in numbers if x % 2 == 0]
print("Even numbers:", even_numbers)
