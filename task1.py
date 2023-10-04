import os 
import sys
import fnmatch

# Handler for invalid inputs
if len(sys.argv) != 3:
    print("Usage: python3 task1.py <path to directory> <file extension>")
elif not os.path.isdir(sys.argv[1]):
    print(f"Directory '{sys.argv[1]}' does not exists. Provide a valid path to directory")

# Find files
file_list = []
for root, directories, files in os.walk(sys.argv[1]):
    for file in files:  
        if fnmatch.fnmatch(file, f"*.{sys.argv[2]}"):
            file_list.append(os.path.join(root, file))

# Check list and print files if there is
if file_list:
    print("Founded files: ")
    for file_path in file_list:
        print(file_path)
else: 
    print(f"No files with specified '{sys.argv[2]}' extension found in '{sys.argv[1]}'")