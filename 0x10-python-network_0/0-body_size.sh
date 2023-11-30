#!/bin/bash
# Get the Content-Length from the response header
curl -sI "$1" | grep -i Content-Length | awk '{print $2}'
