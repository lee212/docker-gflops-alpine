#!/bin/sh
msg=`python /flops.py $@`
echo "{\"system\": {\"hostname\":\"$HOSTNAME\"}, \"msg\": \"$msg\", \"arg\":$@}"
