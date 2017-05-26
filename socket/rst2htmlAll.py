import sys,os 
from glob import glob

for filename in glob('*.rst'):
    htmlname=filename[:-4]+'.html'
    command='rst2html.py %s %s'%(filename,htmlname)
    print command
    os.system(command)
