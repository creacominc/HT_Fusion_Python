#!/usr/bin/env python3

from pprint import pprint

formats = {
    "LowRes": {
        'GuideRatio': 1.77777777777778,
        'Height': 1080.0,
        'Name': 'HD 1080',
        'Rate': 23.97,
        'Width': 1920.0
    },
    "HighRes": {
        'GuideRatio': 1.77777777777778,
        'Height': 2160.0,
        'Name': 'Ultra HD 2160',
        'Rate': 23.97,
        'Width': 3840.0
    }
}


comp = fu.GetCurrentComp()

# change default format for composition

compPrefsFormat = comp.GetPrefs()['Comp']['FrameFormat']

name = compPrefsFormat['Name']
height = compPrefsFormat['Height']
width  = compPrefsFormat['Width']
rate   = compPrefsFormat['Rate']


print( f"Current config - name: {name}, height: {height}, width: {width}, rate: {rate}")

if ( name != formats['HighRes']['Name'] ):
    print( f"replacing global preference with {formats['HighRes']['Name']}" )
    rc = comp.SetPrefs( 
        {
            "Comp.FrameFormat.GuidRatio": formats['HighRes']['GuideRatio'],
            "Comp.FrameFormat.Height": formats['HighRes']['Height'],
            "Comp.FrameFormat.Name": formats['HighRes']['Name'],
            "Comp.FrameFormat.Rate": formats['HighRes']['Rate'],
            "Comp.FrameFormat.Width": formats['HighRes']['Width']
        }
    )


