#!/bin/bash

#### Activity 1: Age ####
###if age is less than 13, return child###
age=$1
child=13
teen=20
adult=65

if [ ${age} -lt ${child} ];
then
	echo "child"
fi

###If age is less than 20, return teen###
if [ ${age} -lt ${teen} ];
then 
	echo "teen"
fi

###If age is less than 65, return adult###
if [ ${age} -lt ${adult} ];
then 
	echo "adult"
fi

###If age is greater than 65, return elderly###
if [ ${age} -gt ${adult} ];
then
	echo "elderly"
fi

