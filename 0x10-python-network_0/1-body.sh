#!/bin/bash
#script that displaus the body of a url get response for code 200
url="$1"; response=$(curl -s -o /dev/null -w "%{http_code}" "$url"); if [ "$response" -eq 200]; then curl -s -X GET "$url" fi
