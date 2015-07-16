#!/usr/bin/env bash

END=23
for i in $(seq 1 $END);
	do python atoh.py $i; 
	# do echo $i;
done
