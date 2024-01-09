#!/bin/bash
# Follow the redirection and print the content
curl -sI "$1" | grep -i "Allow" | cut -d " " -f 2-
