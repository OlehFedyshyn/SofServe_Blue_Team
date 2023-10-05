import sys
import configparser

def parse_ini(ini_file, target_option):
    passwords = {}
    config = configparser.ConfigParser()
    config.read(ini_file)

    for section in config.sections():
        for option in config.options(section):
            if target_option in option.lower():
                passwords[f'{section}.{option}'] = config.get(section, option)

    return passwords

if __name__ == "__main__":
    
    if len(sys.argv) == 1:
       print('Usage python parseIni.py ini-file')
    elif len(sys.argv) == 2:
        target_option = 'password'
        input_file = sys.argv[1]
        
        if input_file.endswith('.ini'):
            answer = parse_ini(input_file,target_option)
            
            if len(answer) > 0:
                print("Finded passwords:")
                for key, value in answer.items():
                    print(f"{key}={value}")
            else :
                print("There is no passwords in this ini-file")
        else:
            print("Input file isn't ini-file")
    else:
         print('Usage python parseIni.py ini-file')
