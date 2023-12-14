#!/bin/bash

# Check if a search string was passed in the command line argument
if [ -z "$1" ]; then
    echo "Please provide a search string as an argument."
    exit 1
fi

# Define the search string
search_string="$1"

# Use mdfind to find applications
apps=$(mdfind kMDItemContentTypeTree=com.apple.application-bundle)

# Loop through each app
while read -r app; do
    bundle_id=$(osascript -e "id of app \"$app\"")
    if [[ $bundle_id == *$search_string* ]]; then
        echo "Found matching ID: $bundle_id for app \"$app\""
    fi
done <<< "$apps"
