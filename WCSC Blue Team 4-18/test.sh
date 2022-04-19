#!/bin/bash
trap bashtrap INT 

bashtrap()
{
	echo "CTRL+C Detected, Exiting.. " && exit
}

#echo "Enter an IP address: "
#read IP
for IP in 10.0.2.{1..254}
do
	ping -c 2 -t 30  $IP > /dev/null && echo "${IP} is up";
done

