#!/usr/bin/python

import subprocess
import sys

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


