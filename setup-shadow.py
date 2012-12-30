#!/usr/bin/python

import subprocess
import sys
import shutil

if sys.version_info < (2,7):
	def check_output(cmd):
		process = subprocess.Popen( cmd, stdout=subprocess.PIPE )
		(stdoutdata,stderrdata) = process.communicate()
		if process.returncode != 0:
			raise subprocess.CalledProcessError(0,cmd,stdoutdata)
		return stdoutdata
else:
	check_output = subprocess.check_output

# see if we are running on shadow..
if check_output("hostname").strip() != "shadow":
	exit(0)

# config for gethub... silly since the files came from there...sigh..
# chicken and egg issue... 
subprocess.check_call( './setup-git-for-github.py' )

# copy hosts file in to place
# TODO: make this generate dynamically instead
shutil.copyfile( './files-for-shadow/hosts', '/etc' )
shutil.copyfile( './files-for-shadow/avrdude.conf', '/etc' )
shutil.copyfile( './files-for-shadow/toshibabacklight', '/etc/init.d')

try:
	os.mkdir( '/etc/powersave' )
except OSError:
	pass
shutil.copyfile( './files-for-shadow/sleep', '/etc/powersave' )

