#!/bin/bash

# Check if the correct number of arguments are provided
if [ $# -ne 2 ]; then
  echo "Expect 2 parameters but $# were given."
  exit 1
fi

# Get 2 args
directory="$1"
extension="$2"

# Check if the directory exists
if [ ! -d "$directory" ]; then
  echo "directory '$directory' does not exists"
  exit
fi 

# Find files and print the result
find "$directory" -type f -name "*.$extension"