import argparse
import os


def search_files(directory, search_text):
    matching_files = []
    for root, _, files in os.walk(directory):
        for file in files:
            file_path = os.path.join(root, file)
            try:
                with open(file_path, "r", encoding="utf-8") as f:
                    if search_text in f.read():
                        matching_files.append(file_path)
            except UnicodeDecodeError:
                pass
            except PermissionError:
                pass
    return matching_files


def main():
    parser = argparse.ArgumentParser(
        description="Search for files containing specified text in a directory."
    )
    parser.add_argument(
        "-p", "--path", required=True, help="Directory path to search for files."
    )
    parser.add_argument(
        "-s", "--search", required=True, help="Text to search for in files."
    )

    args = parser.parse_args()

    directory = args.path
    search_text = args.search

    if not os.path.isdir(directory):
        print(f"Error: '{directory}' is not a valid directory.")
        return

    matching_files = search_files(directory, search_text)

    if matching_files:
        print("Matching files:")
        for file in matching_files:
            print(file)
    else:
        print("No matching files found.")


if __name__ == "__main__":
    main()
