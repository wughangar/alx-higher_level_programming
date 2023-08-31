#!/bin/bash
# script that executes a delete request and displays the body fo the response 
url="$1"; response=$(curl -s -X DELETE "$url"); echo "$response"
