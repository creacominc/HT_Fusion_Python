#!/usr/bin/env python3
import os
import shutil

FUSION_COMP_FOLDER = os.path.expanduser( "~/Library/Application Support/Blackmagic Design/Fusion/Scripts" )

# find all the files under Comp and copy them to the library folder
for subdir, dirs, files in os.walk( 'Comp' ):
    for filename in files:
        filepath = subdir + os.sep + filename
        if filepath.endswith(".py") :
            destination = FUSION_COMP_FOLDER + os.sep + os.path.relpath(filepath, 'Comp/')
            print ( f'copy {filepath} to {destination}')
            shutil.copyfile( filepath, destination )
