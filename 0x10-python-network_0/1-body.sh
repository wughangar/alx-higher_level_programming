#!/bin/bash
#script that displaus the body of a url get response for code 200
url="$1"; response=$(curl -s -o /dev/null -w "%{http_code}" "$url"); [ "$response" -eq 200 ] && curl -s -X GET "$url" || echo "Request did not return a 200 OK response."
