#!/bin/bash

echo -e "\e[31;107mLISTENING CONNECTIONS\E[0m"

netstat -tulpn | grep -i "listen" -B 1 | while read -r line ; do
echo "$line"
done

echo -e "\e[31;107mESTABLISHED CONNECTIONS\E[0m"
netstat -tupn | grep -i "established" -B 1 | while read -r line ; do
echo "$line"
done

