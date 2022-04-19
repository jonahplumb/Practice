#!/bin/bash

echo -e "\e[31;107mROOT Processes\E[0m"

ps a -U root -u root | while read -r line ; do
echo "$line"
done


echo -e "\e[31;107mOther Processes\E[0m"

ps -U root -u root -N | while read -r line ; do
echo "$line"
done
