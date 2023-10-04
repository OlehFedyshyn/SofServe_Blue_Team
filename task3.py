import os
import sys

def count_files_by_extension(directory_path, extension):
    try:
        count = 0
        for root, dirs, files in os.walk(directory_path):
            for file in files:
                if file.endswith('.' + extension):
                    count += 1
        return count
    except Exception as e:
        print('An error occurred:', str(e))
        return -1  
    
if __name__ == "__main__":
    if len(sys.argv) < 3:
        print('Usage: python task3.py <directory_path> <extension>')
    elif len(sys.argv) > 3: 
        print('You should use 2 arguments')
    else:   
        directory_path = sys.argv[1]
        extension = sys.argv[2]
        file_count = count_files_by_extension(directory_path, extension)
        if file_count >= 0:
            print(f'Number of files with extension .{extension} in folder {directory_path}: {file_count} files')
            