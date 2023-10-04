#!/bin/bash

usage(){
	cat << EOF
Usage: $0 path ext
path: Path to the directory
ext: File extension
EOF
}

if [ $# -ne 2 ]; then
	echo "Expect 2 parameters but $# were given."
	usage
	exit 1
fi

# Get user parameters
path="$1"
ext="$2"

if [ ! -d "$path" ]; then
        echo "Path \"$path\" does not exist!"
        exit 1
fi

cat << EOF
Count files with extension "$ext" in "$path": \
$(\
find "$path"\
	-maxdepth 1\
       	-name "*.$ext"\
	-type f\
	| wc -l)
EOF
