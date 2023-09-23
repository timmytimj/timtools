#!/bin/bash
curl -s https://check.torproject.org/exit-addresses | awk '/ExitAddress/ {print $2}' | sort -n

