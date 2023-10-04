# Libraries
# Perform various file or directory-related cases
import os 
# Fnmatch for providing a patter for our files, like ".*txt"
import fnmatch

# Input path to directory  
while True:
    directory = input("Enter the directory: ")
    
    # Check if directory exists
    if not os.path.isdir(directory) :
        print("Directory '{directory}' does not exists. Provide a valid path to directory")
    else:
        break

extension = input("Enter the file extension: ")

# Find files
file_list = []
for root, directories, files in os.walk(directory):
    for file in files:  
        if fnmatch.fnmatch(file, f"*.{extension}"):
            file_list.append(os.path.join(root, file))

# Check list and print files if there is
if file_list:
    print("Founded files: ")
    for file_path in file_list:
        print(file_path)
else: 
    print(f"No files with specified '{extension}' extension found in '{directory}'")