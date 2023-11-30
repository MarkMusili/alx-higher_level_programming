#!/usr/bin/bash
# Get the Content-Length from the response header

if [ -z "$1" ]; then
	echo "Usage $0 <url>"
	exit 1
fi

url=$1

curl -sI "$url" | grep -i Content-Length | awk '{print $2}'