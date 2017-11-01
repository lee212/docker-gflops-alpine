#!/bin/sh
msg=`python /flops.py $@`
echo "{\"msg\": \"$msg\", \"arg\":$@}"
