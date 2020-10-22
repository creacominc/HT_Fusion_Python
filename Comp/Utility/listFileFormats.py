#!/usr/bin/env python3

from pprint import pprint
# this example will print out all of the 
# image formats supported by this copy 
# of Fusion

reg = fusion.GetRegList(comp.CT_ImageFormat)

reg[ 'Attrs' ] = {}
for i in range(1, len(reg)) :
    reg[ 'Attrs' ][i] = fusion.GetRegAttrs(reg[i].ID)
    name = reg[ 'Attrs' ][i][ 'REGS_MediaFormat_FormatName' ]

    if name == None :
        name = reg[ 'Attrs' ][i][ 'REGS_Name' ]

    if reg[ 'Attrs' ][i][ 'REGB_MediaFormat_CanSave' ] == True :
        print(name)
    else:
        print( f'{name} (Cannot Save)' )
