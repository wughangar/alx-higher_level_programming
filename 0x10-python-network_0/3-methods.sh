#!/bin/bash
# script that takes in a URL and displays all HTTP methods the server will accept
url="$1"; methods=$(curl -s -I -X OPTIONS "$url" | grep -i "Allow" | awk '{print $2}'); echo "$methods"
