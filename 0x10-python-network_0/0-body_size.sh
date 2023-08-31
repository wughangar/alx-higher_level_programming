#!/bin/bash
# bash scipt that takes url and displays size of the body
url="$1"; response=$(curl -s "$url"); echo -n "$response" | wc -c
