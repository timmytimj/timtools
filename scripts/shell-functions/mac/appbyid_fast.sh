#!/bin/bash

# Function to extract the bundle ID from an app's Info.plist
get_bundle_id () {
    /usr/libexec/PlistBuddy -c "Print CFBundleIdentifier" "$1/Contents/Info.plist" 2>/dev/null 
}

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
    bundle_id=$(get_bundle_id "$app")
    if [[ $bundle_id == *$search_string* ]]; then
        echo "Found matching bundle ID: $bundle_id for app \"$app\""
    fi
done <<< "$apps"
