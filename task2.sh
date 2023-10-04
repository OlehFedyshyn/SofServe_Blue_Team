#!/bin/bash

usage(){
	cat << EOF
Usage: $0 path text
path: Path to the directory
text: Text to search
EOF
}

if [ $# -ne 2 ];then
	echo "Expect 2 parameters but $# were given."
	usage
	exit 1
fi

# Get user parameters
path="$1"
text="$2"

if [ ! -d "$path" ]; then
	echo "Path \"$path\" does not exist!"
	exit 1
fi

cat << EOF
Looking for the files in "$path",
which has the following text: "$text"
EOF

# Filter files by text
grep -l "$text"\
       	$(find $path -maxdepth 1 -type f)


