import os
import sys


def find_files_with_text(directory, text):
    matching_files = []

    for root, _, files in os.walk(directory):
        for file_name in files:
            file_path = os.path.join(root, file_name)
            try:
                with open(file_path, "r", encoding="utf-8") as file:
                    file_contents = file.read()
                    if text in file_contents:
                        matching_files.append(file_path)
            except Exception:
                pass
                # print(f"Error reading {file_path}")

    return matching_files


def main():
    if len(sys.argv) != 3:
        print("Usage: python search_files.py <directory> <text_to_search>")
        sys.exit(1)

    directory = sys.argv[1]
    text_to_search = sys.argv[2]

    if not os.path.isdir(directory):
        print(f"Error: {directory} is not a valid directory.")
        sys.exit(1)

    matching_files = find_files_with_text(directory, text_to_search)

    if matching_files:
        print("Files containing the specified text:")
        for file in matching_files:
            print(file)
    else:
        print("No files found containing the specified text.")


if __name__ == "__main__":
    main()
