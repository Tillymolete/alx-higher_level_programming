#!/bin/bash
# A script that sends a POST request to url
curl -s "$1" -X POST -d "email=test@gmail.com&subject=I will always be here for PLD"
