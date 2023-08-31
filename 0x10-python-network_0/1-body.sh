#!/bin/bash
#script that displaus the body of a url get response for code 200
url="$1"; curl -s "$url" | wc -c
