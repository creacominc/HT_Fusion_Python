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
        comp.Stop()
        comp.Lock()
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
                # pprint( f'      --- input name: {toolInput.Name}, ID: {toolInput.ID}, data type: {toolInput.GetAttrs("INPS_DataType")}    control page: {toolInput.GetAttrs("INPS_ICS_ControlPage")}' )
                # if ( toolInput.ID == 'OutputSize' ) :
                #     pprint( tool.GetInput( toolInput.Name ) )
                #     pprint( toolInput.GetAttrs() )
                if ( toolInput.ID == 'Width'  or  toolInput.ID == 'MaskWidth' ) :
                    tool.SetInput( toolInput.Name, formats['LowRes']['Width'] )
                elif ( toolInput.ID == 'Height' or  toolInput.ID == 'MaskHeight' ) :
                    tool.SetInput( toolInput.Name, formats['LowRes']['Height'] )
        comp.Unlock()

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
    comp.Stop()
    comp.Lock()
    if ( name != formats['LowRes']['Name'] ):
        print( f"Replacing global preference with {formats['LowRes']['Name']}" )
        rc = comp.SetPrefs(
            {
                "Comp.FrameFormat.GuidRatio": formats['LowRes']['GuideRatio'],
                "Comp.FrameFormat.Height": formats['LowRes']['Height'],
                "Comp.FrameFormat.Name": formats['LowRes']['Name'],
                "Comp.FrameFormat.Rate": formats['LowRes']['Rate'],
                "Comp.FrameFormat.Width": formats['LowRes']['Width']
            }
        )
    comp.Unlock()

def main() :
    comp = fu.GetCurrentComp()
    comp.StartUndo("Switching to Low Res")
    changeDefault( comp )
    changeAllTools( comp )
    comp.EndUndo(True)

if __name__ == "__main__" :
    main()
