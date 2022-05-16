#!/bin/bash

> oldFiles.txt

files=$(grep " jane " /home/student-01-dffb12fc59b6/data/list.txt | cut -d ' ' -f 3)

for i in $files;do

if test -e ~/$i;then

echo $i>>oldFiles.txt;

else echo "not working"; fi

done
