#!/bin/bash
# Follow the redirection and print the content
curl -sI "$1" | grep -i Allow | awk '{print $2" "$3" "$4}'
