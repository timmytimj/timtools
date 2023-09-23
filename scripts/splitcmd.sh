#!/bin/bash

# Path to the file containing the list of commands
file_path="script.txt"

# Number of commands per group
commands_per_group=20

# Prefix for the new files
file_prefix="nd_"

# Subdirectory to store the new files
subdirectory="grab"

# Create the subdirectory, if it doesn't exist
mkdir -p "$subdirectory"

# Split the script into groups of commands
sed -e '/./{H;$!d;}' -e 'x;/./!d;' "$file_path" | awk "
    NR % $commands_per_group == 1 {
        file_number = int(NR / $commands_per_group) + 1
        file_name = \"$subdirectory/$file_prefix\" file_number \".txt\"
        close(output_file)
        output_file = file_name
    }
    { print > output_file }
" -

echo "Splitting and grouping the commands is done!"

