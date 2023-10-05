import xml.etree.ElementTree as ET
import os
import sys

tag_elements = []


def find_tag(element, tag):
    tag_elements.extend(element.findall(tag))

    for child_element in element:
        find_tag(child_element, tag)


def main():
    if len(sys.argv) < 2:
        print(f"Usage: python {sys.argv[0]} <path_to_xml> <tag>(default: 'password')")
        sys.exit(1)

    file_path = sys.argv[1]
    tag = sys.argv[2] if len(sys.argv) >= 3 else "password"

    if not os.path.isfile(file_path):
        print(f"Error: {file_path} is not a valid path.")
        sys.exit(1)

    tree = ET.parse(file_path)
    root = tree.getroot()

    find_tag(root, tag)

    if not tag_elements:
        print(f"'{tag}' tag is not found!")
        sys.exit(1)

    for tag_element in tag_elements:
        if len(tag_element) == 0:
            print(f"'{tag_element.tag}': '{tag_element.text}'")
        else:
            print(f"'{tag_element.tag}': '{''.join(tag_element.itertext()).strip()}'")


if __name__ == "__main__":
    main()
