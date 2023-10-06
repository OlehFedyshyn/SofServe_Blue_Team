import json
import sys
import os
   
def isJson(given_file):
    if not given_file.endswith(".json"):
        print("Usage: File must be in .json format")
        return False
    
    if not os.path.exists(given_file):
        print(f"File '{given_file}' not found")
        return False
    
    return True

# Find key
def findKey(json_data, key_to_find):
    stack = [(json_data, [])]
    results = []

    while stack:
        current_data, current_path = stack.pop()

        # Check, if currect current data is JSON object
        if isinstance(current_data, dict):  
            for key, value in current_data.items():
                if key == key_to_find:
                    results.append((current_path + [key], value))
                # Make sure that we continue explore nested objects
                stack.append((value, current_path + [key]))
        elif isinstance(current_data, list):
            for i, item in enumerate(current_data):
                stack.append((item, current_path + [str(i)]))

    return results

def main(): 
    # Check if it's 3 args provided
    if len(sys.argv) != 3:
        print("Usage: python3 task2.py <path to json file> <key>")
        sys.exit(1);     

    file = sys.argv[1]
    key = sys.argv[2]

    if isJson(file):
        with open(file, 'r') as json_file:
            data = json.load(json_file)
    else:
        exit(1)

    found_keys = findKey(data, key) 
    
    if found_keys:
        searched_key = key if len(found_keys) == 1 else "keys"
        print(f"{len(found_keys)} {searched_key} found:")
        for key, value in found_keys:
            print(f"'{value}'")
    else:
        print(f"Key '{key}' not found in the JSON data.")  

if __name__ == "__main__":
    main()
