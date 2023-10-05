import argparse
import os
import csv

def column_exists(csv_file, column_name):
    try:
        with open(csv_file, newline='') as file:
            reader = csv.DictReader(file)

            if column_name in reader.fieldnames:
                print(f" {column_name}")
                print("---------------------------------")
                for row in reader:
                    print(row[column_name])
                return True
            else:
                return False
    except FileNotFoundError:
        return False

if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Search for specified key elements in a CSV file."
    )
    parser.add_argument(
        '-f', '--file', required=True, help="Path to the CSV file."
    )
    parser.add_argument(
        '-k', '--key', required=True, help="Key to search."
    )

    args = parser.parse_args()
    csv_file = args.file
    column_name = args.key

    if not os.path.isfile(csv_file):
        print(f'Error: \'{csv_file}\' is not a valid file.')
    elif column_exists(csv_file, column_name):
        print("Done")
    else:
        print(f"The column '{column_name}' does not exist in the CSV file.")
