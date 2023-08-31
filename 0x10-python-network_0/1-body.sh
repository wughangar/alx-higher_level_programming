#!/bin/bash
#script that displaus the body of a url get response for code 200
curl -s -X GET $1 | wc -c
