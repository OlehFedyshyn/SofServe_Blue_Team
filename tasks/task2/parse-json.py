import json
import sys

# Handle provided file
def isJson(given_file):
    if not given_file.endswith(".json"):
        print("Usage: File must be in .json format")
        return False
    
    try: 
        with open(given_file, 'r'):
            return True
    except (FileNotFoundError):
        print(f"File '{given_file}' not found")
        return False

# Find key
def findKey(json_data, key_to_find):
    keys_list = []
    for item in json_data:
        if key_to_find in item:
            keys_list.append((key_to_find, item[key_to_find]))
    return keys_list

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