#!/bin/bash

for i in {100000,100,1000,10000}
do
	echo `./jt_list.py 1 $i`
done
