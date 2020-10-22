#!/usr/bin/env python3

import sys
import os
import subprocess

print (sys.version)
pwd = subprocess.check_output( ['pwd'] )
print( f'PWD: {pwd}' )
