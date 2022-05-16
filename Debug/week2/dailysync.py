#!/usr/bin/env python
from multiprocessing import Pool
import os
import subprocess

global src
   src = "{}/data/prod/".format(os.getenv("HOME"))
def sync_data(folder):

   dest = "{}/data/prod_backup/".format(os.getenv("HOME"))
   subprocess.call(["rsync", "-arq", folder, dest])
   print("Handling {}".format(folder))

if __name__ == __main__
   folder = []
   root = next(os.walk(src))[0]
   dirs = next(os.walk(src))[1]

   for dir in dirs:
      folder.append(os.path.join(root,dir))
   pool = Pool(len(folders)) if len(folders) != 0 else Pool(1)
   pool.map(sync_data, folders)
