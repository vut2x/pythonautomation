#!/usr/bin/env python3
import sys
import subprocess
f= open (sys.argv[1],"r")
path='/home/student-01-dffb12fc59b6'
for line in f.readlines():
 old_name = line.strip()
 new_name = old_name.replace("jane","jdoe")
 subprocess.run(["mv",path+old_name,path+new_name])
f.close()
