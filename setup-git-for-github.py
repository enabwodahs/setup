#!/usr/bin/python

import os

os.system('git config --global user.name "enabwodahs"')
os.system('git config --global user.email "github@colberts.us"')
os.system('git config --global credential.helper cache')
os.system("git config --global credential.helper 'cache --timeout=3600'")
