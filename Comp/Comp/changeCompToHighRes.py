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

def changeAllTools( comp ) :
    # update every tool in the composition
    for tool in comp.GetToolList().values() :
        pprint( '' )
        pprint( f'Tool ID: {tool.ID},  Name: {tool.Name}' )
        # Some Attributes will not be visible until the tool is shown in one of the windows.
        # Select and show this tool in window 1
        comp.SetActiveTool( tool )
        comp.CurrentFrame.ViewOn( tool, 2 )
        #
        toolAttrs = tool.GetAttrs()
        #pprint( f" --------- Tool attributes: {toolAttrs}" )
        if 'TOOLI_ImageWidth' in toolAttrs :
            pprint( f'               imageWidth:   {tool.GetAttrs("TOOLI_ImageWidth")}' )
            pprint( f'               imageHeight:  {tool.GetAttrs("TOOLI_ImageHeight")}' )
        inputs = tool.GetInputList().values()
        for toolInput in inputs :
            if ( toolInput.GetAttrs("INPS_ICS_ControlPage") == 'Image' ) :
                if ( toolInput.ID == 'Width' ) :
                    tool.SetInput( toolInput.Name, formats['HighRes']['Width'] )
                if ( toolInput.ID == 'Height' ) :
                    tool.SetInput( toolInput.Name, formats['HighRes']['Height'] )

def changeDefault( comp ) :
    '''
    set the default for the composition to low res so that added tools get the low res setting
    '''
    compAttrs = comp.GetAttrs()
    pprint( '' )
    # report the name and file
    compName = compAttrs['COMPS_Name'].strip()
    compFile = compAttrs['COMPS_FileName'].strip()
    pprint( f'Composition Name: {compName}' )
    pprint( f'            Path: {compFile}' )
    # report the current format
    compPrefs = comp.GetPrefs()
    compPrefsFormat = compPrefs['Comp']['FrameFormat']
    name = compPrefsFormat['Name']
    height = compPrefsFormat['Height']
    width  = compPrefsFormat['Width']
    rate   = compPrefsFormat['Rate']
    print( f"            Current config - name: {name}, height: {height}, width: {width}, rate: {rate}")
    if ( name != formats['HighRes']['Name'] ):
        print( f"Replacing global preference with {formats['HighRes']['Name']}" )
        rc = comp.SetPrefs(
            {
                "Comp.FrameFormat.GuidRatio": formats['HighRes']['GuideRatio'],
                "Comp.FrameFormat.Height": formats['HighRes']['Height'],
                "Comp.FrameFormat.Name": formats['HighRes']['Name'],
                "Comp.FrameFormat.Rate": formats['HighRes']['Rate'],
                "Comp.FrameFormat.Width": formats['HighRes']['Width']
            }
        )

def main() :
    comp = fu.GetCurrentComp()
    comp.Stop()
    comp.Lock()
    comp.StartUndo("Switching to High Res")
    changeDefault( comp )
    changeAllTools( comp )
    comp.EndUndo(True)
    comp.Unlock()

if __name__ == "__main__" :
    main()
