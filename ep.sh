#!/bin/sh
msg=`python /flops.py $@`
uptime=`uptime`
curr_time=`date`
echo "{\"system\": {\"hostname\":\"$HOSTNAME\", \"uptime\":\"$uptime\", \"curr_time\":\"$curr_time\"}, \"msg\": \"$msg\", \"arg\":$@}"
