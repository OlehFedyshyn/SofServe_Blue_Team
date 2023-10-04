#!/bin/bash

# Provide 2 args for directory and file
directory="$1"
extension="$2"

# Input data
read -p "Enter the directory: " directory
read -p "Enter the file extension: " extension

# Check if the directory exists
if [ ! -d "$directory" ]; then
  echo "directory '$directory' does not exists"
  exit
fi 

# Find files and print the result
find "$directory" -type f -name "*.$extension"