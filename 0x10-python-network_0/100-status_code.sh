#!/bin/bash

url=$1
curl -s -o /dev/null -w "%{http_code}" "$url"
