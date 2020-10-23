'''
Get the height, width, and name of the current FrameFormat and lower it to 1080p for faster renders.
'''
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

pprint( fu ) 

compPrefsFormat = fu.GetPrefs()['Comp']['FrameFormat']
name = compPrefsFormat['Name']
height = compPrefsFormat['Height']
width  = compPrefsFormat['Width']
rate   = compPrefsFormat['Rate']

print( f"Current config - name: {name}, height: {height}, width: {width}, rate: {rate}")

if ( name != formats['LowRes']['Name'] ):
    print( f"replacing global preference with {formats['LowRes']['Name']}" )
    rc = fu.SetPrefs( 
        {
            "Comp.FrameFormat.GuidRatio": formats['LowRes']['GuideRatio'],
            "Comp.FrameFormat.Height": formats['LowRes']['Height'],
            "Comp.FrameFormat.Name": formats['LowRes']['Name'],
            "Comp.FrameFormat.Rate": formats['LowRes']['Rate'],
            "Comp.FrameFormat.Width": formats['LowRes']['Width']
        }
    )
    print( f"result: {rc}" )
    if( rc ) :
        fu.SavePrefs()



compPrefsFormat = fu.GetPrefs()['Comp']['FrameFormat']
name = compPrefsFormat['Name']
height = compPrefsFormat['Height']
width  = compPrefsFormat['Width']
rate   = compPrefsFormat['Rate']

print( f"Current config - name: {name}, height: {height}, width: {width}, rate: {rate}")
