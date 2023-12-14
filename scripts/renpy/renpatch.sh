#!/bin/bash

file='/Users/tim/tmp/~dirtyConsole.rpy'
selectedApp="$1"

if [ -z "$selectedApp" ]; then
    echo "No app package selected!"
else
    appPath="$selectedApp/Contents/Resources/autorun/game/"
    cp "$file" "$appPath"
fi
