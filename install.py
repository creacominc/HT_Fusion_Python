#!/usr/bin/env python3
import os
import shutil

FUSION_USER_DIR    = "~/Library/Application Support/Blackmagic Design/Fusion/"
FUSION_CONFIG_DIR  = os.path.expanduser( f"{FUSION_USER_DIR}Config" )
FUSION_COMP_FOLDER = os.path.expanduser( f"{FUSION_USER_DIR}Scripts" )

# find all the config files under Config and copy them to the library folder
for subdir, dirs, files in os.walk( 'Config' ):
    for filename in files:
        filepath = subdir + os.sep + filename
        if filepath.endswith(".fu") :
            destination = FUSION_CONFIG_DIR + os.sep + os.path.relpath(filepath, 'Config/')
            print ( f'copy {filepath} to {destination}')
            shutil.copyfile( filepath, destination )

# find all the files under Comp and copy them to the library folder
for subdir, dirs, files in os.walk( 'Comp' ):
    for filename in files:
        filepath = subdir + os.sep + filename
        if filepath.endswith(".py") :
            destination = FUSION_COMP_FOLDER + os.sep + os.path.relpath(filepath, 'Comp/')
            print ( f'copy {filepath} to {destination}')
            shutil.copyfile( filepath, destination )
