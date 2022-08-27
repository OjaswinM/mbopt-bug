#!/bin/bash

DIR="./mnt"
BS=4096
BLK_PER_GRP=$(( $BS * 8 ))


find $DIR -exec bash -c "filefrag -v {} | tail -n +4 | head -n -1 | \
	awk '{ print int(substr(\$4, 1, length(\$4)-2) / $BLK_PER_GRP) }'" \; 2>/dev/null

# echo $OP | \
# while read block 
# do
# 	echo &(( $block / $BLK_PER_GRP ))
# done	
