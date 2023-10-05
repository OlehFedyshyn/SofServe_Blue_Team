import os 
import sys
import fnmatch

try:
    if len(sys.argv) != 3:
        raise ValueError("Usage: python3 task1.py <path to directory> <file extension>")
    elif not os.path.isdir(sys.argv[1]):
        raise ValueError(f"Directory '{sys.argv[1]}' does not exist. Provide a valid path to a directory")

    # Find files
    file_list = []
    for root, directories, files in os.walk(sys.argv[1]):
        for file in files:
            if fnmatch.fnmatch(file, f"*.{sys.argv[2]}"):  # Use sys.argv[2] for the file extension
                file_list.append(os.path.join(root, file))

    # Check list and print files if there are any
    if file_list:
        print("Found files:")
        for file_path in file_list:
            print(file_path)
    else: 
        print(f"No files with specified '{sys.argv[2]}' extension found in '{sys.argv[1]}'")

except ValueError as err:
    print(err)



