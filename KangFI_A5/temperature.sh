#!/bin/bash

####Activity 2: Temperature in California####
###If the temperature is greater than 55, but less then 67, return cold###
temp=$1
cold=55
normal=67
hot=85

if [ ${temp} -gt ${cold} ] && [ ${temp} -lt ${normal} ];
then
	echo "cold"
fi	       

###If the temperature is less than 85, but greater then 67, return nice###
if [ ${temp} -lt ${hot} ] && [ ${temp} -gt ${normal} ];
then 
	echo "nice"
fi

###If the temperature is greater than 85, return hot###
if [ ${temp} -gt ${hot} ];
then 
	echo "hot"
fi

###If the temperature is less than 55, return freezing###
if [ ${temp} -lt ${cold} ];
then 
	echo "freezing"
fi
