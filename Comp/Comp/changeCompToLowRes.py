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

def changeAllTools() :
    # outputs the name of every tool in the composition
    comp = fu.GetCurrentComp()
    #pprint(comp.GetToolList())
    # print all tool names and ids
    for tool in comp.GetToolList().values() :
        if (tool.Name == 'Text1') :
            pprint( f'Tool ID: {tool.ID},  Name: {tool.Name}' )
            #
            '''
            #
            pprint( f" --------- Tool attributes: {tool.GetAttrs()}" )
            #
            Tool attributes: {'TOOLB_ShowControls': False, 'TOOLS_Name': "
            "'Text1', 'TOOLB_Visible': True, 'TOOLB_Locked': False, 'TOOLB_PassThrough': "
            "False, 'TOOLB_HoldOutput': False, 'TOOLB_CtrlWZoom': False, 'TOOLB_NameSet': "
            "False, 'TOOLB_CacheToDisk': False, 'TOOLB_Selected': False, 'TOOLS_RegID': "
            "'TextPlus', 'TOOLI_ID': 62.0, 'TOOLN_LastFrameTime': 0.0, "
            "'TOOLI_Number_o_Inputs': 0.0, 'TOOLNT_EnabledRegion_Start': {1.0: "
            "-1000000000.0}, 'TOOLNT_EnabledRegion_End': {1.0: 1000000000.0}, "
            "'TOOLNT_Region_Start': {1.0: 0.0}, 'TOOLNT_Region_End': {1.0: 1000.9999}}")
            '''

            #
            # Inputs
            #
            pprint( f" ~~~~~~~~ Inputs  for {tool.Name}" )
            inputs = tool.GetInputList().values()
            for toolInput in inputs :
                if( toolInput.ID == "Width" or toolInput.ID == "Height" ) :
                    pprint( f'    name: {toolInput.Name}, ID: {toolInput.ID}', data type: {toolInput.GetAttrs("INPS_DataType")}' )
                    #pprint( f'       id:  {toolInput.GetID()}' )
                    #
                    '''
                    #
                    pprint( f'  tool input attributes  ---> : {toolInput.GetAttrs()}')
                    #
                    ("  tool input attributes  ---> : {'INPS_Name': 'Width', 'INPS_ID': 'Width', "
                    "'INPS_DataType': 'Number', 'INPB_External': True, 'INPB_Active': False, "
                    "'INPB_Required': True, 'INPB_Connected': False, 'INPI_Priority': 0.0, "
                    "'INPID_InputControl': 'SliderControl', 'INPB_Disabled': False, "
                    "'INPB_DoNotifyChanged': True, 'INPB_Integer': True, 'INPI_NumSlots': 1.0, "
                    "'INPB_ForceNotify': False, 'INPB_InitialNotify': False, 'INPB_Passive': "
                    "False, 'INPB_InteractivePassive': False, 'INPB_SendRequest': True, "
                    "'INPB_GetRequirements': True, 'INPB_ForceSecondaryTimeNotify': False, "
                    "'INPN_MinAllowed': 1.0, 'INPN_MaxAllowed': 32767.0, 'INPN_MinScale': 1.0, "
                    "'INPN_MaxScale': 4096.0, 'INPI_IC_ControlGroup': 0.0, 'INPI_IC_ControlID': "
                    "0.0, 'INPI_IC_ControlPage': 0.0, 'INPI_PC_ControlGroup': 0.0, "
                    "'INPI_PC_ControlID': 0.0, 'INPS_ICS_ControlPage': 'Image', 'INPB_OpMenu': "
                    "True, 'INPB_IC_TimeType': False, 'INPB_IC_StepRestrict': False, "
                    "'INPB_IC_Visible': False, 'INPB_PC_Visible': False, "
                    "'INPB_PC_FastSampleRate': False, 'INPI_UserData': 0.0, 'INPI_SubType': 0.0, "
                    "'INPI_IC_Steps': 4097.0, 'INPI_IC_DisplayedPrecision': 0.0, "
                    "'INPI_PC_GrabPriority': 0.0, 'INPN_Default': 1920.0, 'INPN_DefaultX': 0.0, "
                    "'INPN_DefaultY': 0.0, 'INPN_UserData2': 0.0, 'INPN_UserData3': 0.0, "
                    "'INPN_IC_Center': 0.0, 'INPN_ICD_Width': 0.0, 'INPI_IC_FixedWidth': 0.0, "
                    "'INPB_IC_ForceWrap': False, 'INPB_IC_SkipNest': False, 'INPB_IC_NoLabel': "
                    "0.0, 'INPB_IC_NoReset': 0.0, 'INPB_IgnoreVisible': 0.0, 'INPI_IC_TickSteps': "
                    '0.0}')
                    '''
            #

            '''
             outputs
                 ---> : {'OUTS_Name': 'Output', 'OUTS_DataType': 'Image', 'OUTS_ID': 'Output'}
            '''
            pprint( f' +++++ outputs' )
            outputs = tool.GetOutputList().values()
            for toolOutput in outputs :
                outputAttrs = toolOutput.GetAttrs()
                pprint( f'    ---> : {outputAttrs}' )
                outsDataType = outputAttrs['OUTS_DataType']
                pprint( f'    name: {toolOutput.Name}, ID: {toolOutput.ID}, DataType: {outsDataType}' )
                # pprint( f'  {dir(toolOutput)}')
                # pprint( f'       id:  {toolOutput.GetID()}' )
                #value = toolOutput.GetData( )
            # children = tool.GetChildrenList().values()
            # if( children ) :
            #     pprint( f'Children of {tool.Name}')
            #     for child in children :
            #         pprint( child )
            pprint( f" ^^^^^^^^^  end for {tool.Name}" )



def changeDefault() :
    comp = fu.GetCurrentComp()
    compPrefsFormat = comp.GetPrefs()['Comp']['FrameFormat']
    name = compPrefsFormat['Name']
    height = compPrefsFormat['Height']
    width  = compPrefsFormat['Width']
    rate   = compPrefsFormat['Rate']
    print( f"Current config - name: {name}, height: {height}, width: {width}, rate: {rate}")
    if ( name != formats['LowRes']['Name'] ):
        print( f"replacing global preference with {formats['LowRes']['Name']}" )
        # rc = comp.SetPrefs( 
        #     {
        #         "Comp.FrameFormat.GuidRatio": formats['LowRes']['GuideRatio'],
        #         "Comp.FrameFormat.Height": formats['LowRes']['Height'],
        #         "Comp.FrameFormat.Name": formats['LowRes']['Name'],
        #         "Comp.FrameFormat.Rate": formats['LowRes']['Rate'],
        #         "Comp.FrameFormat.Width": formats['LowRes']['Width']
        #     }
        # )
    changeAllTools()

def main() :
    changeDefault()


if __name__ == "__main__" :
    main()
