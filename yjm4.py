
text = "Hello, World!"


print("Original String:", text)
print("First 5 characters:", text[:5])      
print("Characters 7 to 11:", text[7:12])
print("Last 6 characters:", text[-6:])      


name = "YASH"
age = 21
print("\nUsing f-string:")  
print(f"My name is {name} and I am {age} years old.")

print("\nUsing format() method:")
print("My name is {} and I am {} years old.".format(name, age))


sample = "   Python Programming   "

print("\nOriginal with spaces:", repr(sample))
print("Lowercase:", sample.lower())      
print("Uppercase:", sample.upper())     
print("Stripped:", sample.strip())           
print("Replace 'Python' with 'Java':", sample.replace("Python", "Java"))
print("Does it start with 'Py'? ->", sample.strip().startswith("Py"))
print("Does it end with 'ing'? ->", sample.strip().endswith("ing"))
print("Count of 'm':", sample.count("m"))
print("Split into words:", sample.strip().split())
