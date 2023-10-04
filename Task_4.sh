#!/bin/bash

while getopts "p:t:" flag; do
    case "${flag}" in
        p) path="${OPTARG}" ;;
        t) text="${OPTARG}" ;;
    esac
done

if [ $# -eq 0 ]; then
    echo "Usage: Enter first param(-p) - path, then second param(-t) text"
else
    if [ -z "$path" ]; then
        echo "Error: -p path is empty"
        exit 1
    elif [ ! -e "$path" ]; then
        echo "Error: $path path does not exist"
        exit 1
    elif [ -z "$text" ]; then
        echo "Error: -t text is empty"
        exit 1
        
    else
        grep -R "$text" "$path"
    fi
fi
