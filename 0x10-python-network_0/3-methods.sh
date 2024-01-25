#!/bin/bash
# A script dispying allowed HTTP methods
curl -sI "$1" | grep "Allow" | cut -d " " -f 2-
