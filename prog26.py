#Write a program to perform file and directory operations using os and sys modules

import os
import sys

print("Current Directory:", os.getcwd())
new_dir = "test_folder"
if not os.path.exists(new_dir):
    os.mkdir(new_dir)
    print(f"Directory '{new_dir}' created.")
else:
    print(f"Directory '{new_dir}' already exists.")
print("Contents:", os.listdir())
file_path = os.path.join(new_dir, "sample.txt")
