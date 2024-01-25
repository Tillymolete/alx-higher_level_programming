#!/usr/bin/bin
# A script that takes in a URL, send request and displays body size
curl -sI "$1" | grep -i "content-Length" | awk '{{print $2}'
