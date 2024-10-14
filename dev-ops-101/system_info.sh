#!/bin/bash
num_files=$(find . -maxdepth 1 -type f | wc -l)
date
whoami
echo "Number of files in the current directory: $num_files"
