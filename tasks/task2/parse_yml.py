import yaml

def check_password_key_in_yaml(yaml_file, key_to_check):
    try:
        with open(yaml_file, 'r') as file:
            data = yaml.safe_load(file)
            if key_to_check in data:
                return data[key_to_check]
            else:
                return None
    except FileNotFoundError:
        print(f"Error: File '{yaml_file}' not found.")
        return None
    except Exception as e:
        print(f"An error occurred: {e}")
        return None

if __name__ == "__main__":
    yaml_file = "Hello my Key"
    key_to_check = "password"

    password_value = check_password_key_in_yaml(yaml_file, key_to_check)
    if password_value is not None:
        print(f"The value of '{key_to_check}' is: {password_value}")
    else:
        print(f"'{key_to_check}' key not found in the YAML file.")
