#Write a program to demonstrate iterators and iterables in Python

numbers = [10, 20, 30, 40]

print("Iterable (list):", numbers)

numbers_iterator = iter(numbers)

print("\nAccessing elements using iterator and next():")
while True:
    item = next(numbers_iterator, None) 
    if item is None:
        break
    print(item)

print("\nUsing iterable directly in a for loop:")
for num in numbers:
    print(num)
