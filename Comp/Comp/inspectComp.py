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

def reportOnToolAttrs( tool ) :
    '''
    Sample code to report on attributes for a tool
    '''
    #
    # Attributes
    #
    toolAttrs = tool.GetAttrs()
    # pprint( f" --------- Tool attributes: {toolAttrs}" )
    if 'TOOLI_ImageWidth' in toolAttrs :
        pprint( f'               imageWidth:   {tool.GetAttrs("TOOLI_ImageWidth")}' )
        pprint( f'               imageHeight:  {tool.GetAttrs("TOOLI_ImageHeight")}' )
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


def reportOnInputs( tool ) :
    '''
    Sample code to report on the inputs for a tool
    '''
    #
    # Inputs
    #
    pprint( f"          Inputs  for {tool.Name}" )
    inputs = tool.GetInputList().values()
    #allNames = ''
    #separator = ''
    for toolInput in inputs :
        #allNames += f'{separator}[Name: {toolInput.Name}, ID: {toolInput.ID}, {toolInput.GetAttrs("INPS_DataType")}]'
        #separator = ', '
        pprint( f'      --- input name: {toolInput.Name}, ID: {toolInput.ID}, data type: {toolInput.GetAttrs("INPS_DataType")}    control page: {toolInput.GetAttrs("INPS_ICS_ControlPage")}' )
        #pprint( f'     {toolInput.GetAttrs()}' )
        #pprint( f'       id:  {toolInput.GetID()}' )
        #pprint( f'               control page: {toolInput.GetAttrs("INPS_ICS_ControlPage")}' )
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
        "0.0, "
        "'INPI_IC_ControlPage': 0.0, "
        "'INPI_PC_ControlGroup': 0.0, "
        "'INPI_PC_ControlID': 0.0, "
        "'INPS_ICS_ControlPage': 'Image', "
        "'INPB_OpMenu': "
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
    #pprint( f'          {allNames}')

def reportOnMainInputs( tool ) :
    '''
    Sample code to report on main inputs
    '''
    #
    # main? inputs
    #
    # Loop through all main inputs.
    pprint( f' ======= finding main inputs' )
    i =1
    while True :
        inp = tool.FindMainInput(i)
        if inp is None :
            break
        # Got input
        pprint( f'          Main Input Name: {inp.GetAttrs()["INPS_Name"]}' )
        i+=1
    #

def reportOnOutputs( tool ) :
    '''
    sample code to report on outputs for a tool
    '''
    #
    # outputs
    #
    pprint( f' ++++++++ outputs' )
    outputs = tool.GetOutputList().values()
    for toolOutput in outputs :
        outputAttrs = toolOutput.GetAttrs()
        outsDataType = outputAttrs['OUTS_DataType']
        pprint( f'      +++ output name: {toolOutput.Name}, ID: {toolOutput.ID}, DataType: {outsDataType}' )
        pprint( f'  {dir(toolOutput)}')
        pprint( f'       id:  {toolOutput.GetID()}' )
        #value = toolOutput.GetData( )
        pprint( f'    ---> : {outputAttrs}' )
        '''
        output attributes
            ---> : {'OUTS_Name': 'Output', 'OUTS_DataType': 'Image', 'OUTS_ID': 'Output'}
        '''
        pprint( f'    --- { dir( toolOutput ) }' )
        # -- do not do this, it crashes fusion
        #outputValue = toolOutput.GetValue()
        #pprint( f'      ---- value: {outputValue}' )
        outputData = toolOutput.GetData()
        pprint( f'      ---- data: {outputData}' )
    #

def reportOnUserControls( tool ) :
    '''
    sample code to report on user controls (whatever they are)
    '''
    #
    # user controls
    #
    pprint( f' ------- user controls' )
    for cntrl in tool.UserControls :
        pprint( f'      --- control: {cntrl} ' )
    #

def reportOnChildren( tool ) :
    '''
    sample code to report on children
    '''
    #
    # children
    #
    children = tool.GetChildrenList().values()
    if( children ) :
        pprint( f'Children of {tool.Name}')
        for child in children :
            pprint( child )
    #

def reportOnToolData( tool ) :
    '''
    This does not seem to work.
    '''
    #
    # Get tool data
    #
    toolData = tool.GetData()
    pprint( f'       --- Tool Data: {toolData}' )
    #


def reportOnAllTools( comp ) :
    # outputs the name of every tool in the composition
    for tool in comp.GetToolList().values() :
        pprint( '' )
        pprint( f'Tool ID: {tool.ID},  Name: {tool.Name}' )
        # Some Attributes will not be visible until the tool is shown in one of the windows.
        # Select and show this tool in window 2
        comp.Stop()
        comp.Lock()
        comp.SetActiveTool( tool )
        comp.CurrentFrame.ViewOn( tool, 2 )
        comp.Unlock()
        #
        reportOnToolAttrs( tool )
        # reportOnInputs( tool )
        # reportOnMainInputs( tool )
        # reportOnOutputs( tool )
        # reportOnUserControls( tool )
        # reportOnChildren( tool )
        # reportOnToolData( tool )
        pprint( f" ^^^^^^^^  end for {tool.Name}" )


def reportOnComp( comp ) :
    '''
    sample code to report on the provided composition
    '''
    # Attributes
    compAttrs = comp.GetAttrs()
    pprint( '' )
    compName = compAttrs['COMPS_Name'].strip()
    compFile = compAttrs['COMPS_FileName'].strip()
    pprint( f'Composition Name: {compName}' )
    pprint( f'            Path: {compFile}' )
    '''
    pprint( f' Composition Attributes: {compAttrs}' )
            (" Composition Attributes: {'COMPB_HiQ': True, 'COMPB_MotionBlur': True, "
        "'COMPB_Proxy': False, 'COMPB_Rendering': False, 'COMPB_Modified': False, "
        "'COMPB_Locked': False, 'COMPB_LoopPlay': True, 'COMPN_CurrentTime': 0.0, "
        "'COMPN_RenderStart': 0.0, 'COMPN_RenderEnd': 1000.0, 'COMPN_GlobalStart': "
        "0.0, 'COMPN_GlobalEnd': 1000.0, 'COMPN_RenderStartTime': 0.0, "
        "'COMPN_RenderEndTime': 1000.0, 'COMPN_LastFrameRendered': -2000000000.0, "
        "'COMPN_LastFrameTime': 0.0, 'COMPN_AverageFrameTime': 0.0, "
        "'COMPN_TimeRemaining': 0.0, 'COMPN_ElapsedTime': 0.0, 'COMPN_AudioOffset': "
        "0.0, 'COMPS_FileName': '/Volumes/VideoScratch/VideoProjects/test3.comp', "
        "'COMPS_Name': 'test3.comp', 'COMPS_LoopMode': 'loop', 'COMPI_RenderFlags': "
        "131072.0, 'COMPI_RenderStep': 1.0, 'COMPH_ActiveTool': <PyRemoteObject "
        'object at 0x7ffb2005a510>}')
    '''
    # Data
    '''
    compData = comp.GetData()
    pprint( f' Composition Data: {compData}' )
        ' Composition Data: None'
    '''
    # Preferences
    compPrefs = comp.GetPrefs()
    '''
    pprint( f' Composition Preferences: {compPrefs}' )
        (" Composition Preferences: {'Comp': {'AutoSave': {'Enabled': True, 'Delay': "
        "60.0, 'OnRender': True}, 'NumberStyles': {'Color': 0.0, 'ClipFrame': 0.0}, "
        "'Paths': {'EnableReverseMapping': False}, 'Network': {'SlaveMemOverride': "
        "False, 'DoNetworkRenders': False}, 'LUTView': {'IndependentHandles': False, "
        "'ShowKeyMarkers': False, 'ShowTips': False, 'AutoScaleVal': 1.0}, "
        "'FlowView': {'AspectTilePics': True, 'ForceSource': False, 'ForceActive': "
        "False, 'Scale': 1.0, 'ForceMask': False, 'ForceAll': False, "
        "'ShowInstanceLinks': True, 'RemoveRouters': True, 'ShowNavigator': 2.0, "
        "'AutoSnap': True, 'PipesOnTop': False, 'Direction': 0.0, 'PipeStyle': 1.0, "
        "'ShowHidden': False, 'ConnectedSnap': True, 'ShowThumbnails': True, "
        "'ShowGrid': True, 'GridSnap': True, 'ForceModes': True, 'FullToolIndicator': "
        "False}, 'LastFile': '/Applications/Visual Studio Code.app', 'Interactive': "
        "{'Proxy': {'Scale': 5.0, 'Auto': True, 'AutoScale': 8.0}, "
        "'BackgroundRender': False, 'SelectiveUpdate': 1.0}, 'Bins': {'LoaderBin': "
        "'<none>', 'SaverBin': '<none>'}, 'FrameFormat': {'GuideRatio': "
        "1.77777777777778, 'GuideX2': 1.0, 'TimeCodeRadio': 1.0, 'AspectY': 1.0, "
        "'DepthLock': True, 'GuideY2': 1.0, 'DropFrame': 0.0, 'GuideX1': 0.0, "
        "'TimeCodeType': 0.0, 'Name': 'HD 1080', 'PerFeet': 1.0, 'DepthPreview': 0.0, "
        "'Rate': 23.97, 'Width': 1920.0, 'AspectX': 1.0, 'Fields': False, "
        "'DepthFull': 0.0, 'GuideY1': 0.0, 'Height': 1080.0, 'DepthInteractive': 0.0, "
        "'DepthLoader': 0.0, 'AspectLoader': 0.0}, 'Splines': {'BSplineDegree': 3.0, "
        "'RotoAssistTracking': False, 'OnionSkinPointPlot': False, 'AutoSmoothLUTs': "
        "False, 'AutoSmoothSplines': False, 'DefOnionSkinCount': 10.0, "
        "'TrackerPointsShow': 2.0, 'AutoSmoothPolylines': False, "
        "'BSplinePolylineDegree': 3.0, 'RotoAssist': False, 'OnionSkinAnchor': False, "
        "'TrackerPath': 'PolyPath', 'ExportMode': 16.0, 'PolyLineEditMode': "
        "'InsertAndModify', 'DefOnionSkinStep': 5.0, 'AutoSmoothPaths': False, "
        "'RotoAssistMultiplePts': False, 'OnionSkinShowHull': True, "
        "'SelectPointsFromMultiPolies': True, 'AutoSmoothBSplines': True, "
        "'OnionSkinClickSetCT': False, 'RotoAssistDistance': 8.0, "
        "'DefOnionSkinRange': 3.0, 'AutoSmoothMeshes': True, "
        "'AutoSmoothBSplinePolylines': True}, 'PolyKeyListDlg': {'Window': {'Left': "
        "-1.0, 'Top': -1.0}}, 'SplineEditor': {'IndependentHandles': False, "
        "'ShowKeyMarkers': False, 'AutoSnap': {'Keys': 2.0, 'Guides': 1.0}, "
        "'AutoScale': False, 'FollowActive': False, 'ShowTips': True, 'AutoScaleVal': "
        "1.0}, 'Preview': {'Type': 1.0, 'Scale': True, 'HiQ': True, 'Width': 200.0, "
        "'KeepAspect': True, 'SkipFrames': True, 'ActiveSavers': True, "
        "'OutputDevice': 'Left.A', 'Height': 160.0, 'Depth': 0.0, 'ActiveLoaders': "
        "True, 'SizeType': 1.0}, 'Unsorted': {'GlobalStart': 0.0, 'GlobalEnd': "
        "1000.0}, 'Transport': {'FrameStep': 1.0}, 'Audio': {'Playback': True}, "
        "'ChildFrame': {1.0: {'Mode': 3.0, 'UseWindowsDefaults': True, 'OpenOnNew': "
        "True}}, 'AVI': {'Saver': {'DataCheck': True, 'Key': 15.0, 'Handler': "
        "541215044.0, 'KeyCheck': True, 'DataRate': 300.0, 'Quality': 75.0}}, 'Info': "
        "{'CreateDate': '', 'ModifyDate': '', 'Comments': '', 'Author': '', 'Client': "
        "'', 'Job': ''}, 'FilterModeName': '<unknown>', 'Memory': {'Render': "
        "{'SimultaneousBranching': True}, 'FramesAtOnce': 10.0, 'Interactive': "
        "{'SimultaneousBranching': True, 'ResponseTime': 0.5}}, 'UserInterface': "
        "{'SelectionSync': True}, 'Timeline': {'AutoSnap': {'Keys': 2.0, 'Guides': "
        "-1.0}, 'ViewFilterMode': -1.0}, 'Import': {'EDL': {'FlowFormat': 0.0, "
        "'UseShotNames': 0.0}}, 'Views': {'Defaults': {'MaterialViewer': {'Options': "
        "{'LightPosition': 0.0, 'SurfaceType': 0.0, 'RendererType': 'RendererOpenGL', "
        "'LightingEnabled': True, 'TextureDepth': 'int8'}, 'Camera': {'Rotation': "
        "{'Y': -20.0, 'X': 15.0, 'Z': 0.0}}}, '3DHistogram': {'Proxy': 4.0, 'Log': "
        "False, 'Transparent': True, 'LoopLines': True, 'DrawStyles': 0.0}, "
        "'CheckerUnderlay': False, 'Viewer': {'EnableLUTs': False, 'LUTSelected': '', "
        "'DoD': {'Show': False}, 'CheckerUnderlay': True, 'Normalise': False, "
        "'NearZ': 0.0, 'ID': 'GLImageViewer', 'OverlayColor': 7.0, 'FitMarginX': 0.0, "
        "'Smooth': True, 'SmoothThreshold': 1000000.0, 'ShowLabels': True, 'View360': "
        "0.0, 'Region': {'Show': True, 'Bottom': 0.0, 'Auto': False, 'Lock': False, "
        "'Enable': False, 'Right': 1.0, 'Left': 0.0, 'Top': 1.0}, 'ShowControls': "
        "True, 'Layer': '', 'ScaleMode': 0.0, 'FitMarginY': 0.0, 'One2One': False, "
        "'LUTPlugin': 'FusionViewLUT', 'PixelGrid': False, 'Channel': -1.0, "
        "'AlphaOverlay': False, 'OverlayOpacity': 100.0, 'FarZ': -1000.0, "
        "'FollowActive': False}, 'BgColor': -1.0, 'SubView': {'Enabled': False, "
        "'Navigator': False, 'Magnifier': False, 'ID': 'GLHistogramViewer', "
        "'MagnifierScale': 8.0}, 'FullScreen': False, 'Guides': {'Show': False, "
        "'Center': True, 'SafeTitle': True, 'SafeImage': True, 'Film': False, "
        "'FrameAspect': 'Default'}, 'View3D': {'Options': {'SelectionBoxStipple': "
        "65520.0, 'ShowTextureMemory': False, 'Shadows': False, 'ShowLights': True, "
        "'Lighting': False, 'ShowUVTangentVectors': False, 'ShowPointClouds': True, "
        "'Grid': True, 'ShowFastLabel': False, 'ShowVertexNormals': False, "
        "'ShowMatteObjects': False, 'DefaultLight': True, 'Culling': False, "
        "'ShowCameras': True, 'Wireframe': False, 'SelectionBoxStippleHidden': "
        "52416.0}, 'CamLeft': {'Rotation': {'Y': 90.0, 'X': 0.0, 'Z': 0.0}, 'Scale': "
        "1.0, 'Position': {'Y': 0.0, 'X': 0.0, 'Z': 0.0}}, 'CamPersp': {'Rotation': "
        "{'Y': 0.0, 'X': 30.0, 'Z': 0.0}, 'Scale': 1.0, 'Position': {'Y': 0.0, 'X': "
        "0.0, 'Z': 0.0}}, 'CamRight': {'Rotation': {'Y': -90.0, 'X': 0.0, 'Z': 0.0}, "
        "'Scale': 1.0, 'Position': {'Y': 0.0, 'X': 0.0, 'Z': 0.0}}, 'TextureDepth': "
        "'int8', 'CamFront': {'Rotation': {'Y': 0.0, 'X': 0.0, 'Z': 0.0}, 'Scale': "
        "1.0, 'Position': {'Y': 0.0, 'X': 0.0, 'Z': 0.0}}, 'SortMethod': 'ZBuffer', "
        "'OverscanMode': 0.0, 'CustomOverscan': 1.37, 'CamTop': {'Rotation': {'Y': "
        "0.0, 'X': 90.0, 'Z': 0.0}, 'Scale': 1.0, 'Position': {'Y': 0.0, 'X': 0.0, "
        "'Z': 0.0}}, 'CameraName': 'Perspective'}, 'QuadLayoutName': '4-Way', "
        "'AlwaysOnTop': True, 'QuadView': False, 'Controls': {'Hiding': 0.0, "
        "'Autofade': False, 'FadeSpeed': 1.0, 'SnapPixel': False, 'Opacity': 100.0, "
        "'FadeDelay': 2000.0, 'SnapPixelMode': 0.0, 'StippleHidden': True}, 'Dither': "
        "False, 'PickW': 1.0, 'Vectorscope': {'DrawStyles': 1.0, 'OneLine': False, "
        "'Color': False, 'LoopLines': True, 'SubSampling': 4.0, 'ColorSpace': 0.0}, "
        "'PickH': 1.0, 'VideoOut': False, 'Toolbar': {'Style': 0.0, 'Size': 0.0}, "
        "'PrevCtrlInactiveColor': 4278255360.0, 'Mirror': {'Enable': False, "
        "'StereoMethod': 'Auto', 'Device': ''}, 'Histogram': {'DrawStyles': 0.0, "
        "'Channels': 7.0, 'Scale': 0.0, 'Transparent': False}, 'PrevCtrlActiveColor': "
        "4278190335.0, 'Waveform': {'OneLine': False, 'SubSampling': 4.0, 'Mode': "
        "0.0, 'LoopLines': True, 'ColorSpace': 0.0}, 'ShowClipFrameNumbers': True, "
        "'BufferLUT': {'Enable': False, 'Selected': '', 'Plugin': 'FusionViewLUT'}, "
        "'Stereo': {'Enabled': False, 'Swap': False, 'AnaglyphMethod': 'Color', "
        "'StackMethod': 'Horizontal', 'OffsetX': {'QuadB': 0.0, 'Stack': 0.0}, "
        "'Stack': False, 'DisplayMethod': 'Quad Buffer', 'OffsetY': {'QuadB': 0.0, "
        "'Stack': 0.0}, 'ABSource': False, 'AnaglyphColor': 'Red/Cyan'}, 'OpToolbar': "
        "{'Style': 0.0, 'Size': 0.0}}, 'Right': {'PrevCtrlInactiveColor': "
        "4278255360.0, 'PickW': 1.0, 'PickH': 1.0, 'SideB': {'PrevCtrlInactiveColor': "
        "4278255360.0, 'PickW': 1.0, 'PickH': 1.0, 'PrevCtrlActiveColor': "
        "4278190335.0, 'Viewer': {'EnableLUTs': False, 'LUTPlugin': 'FusionViewLUT', "
        "'NearZ': 0.0, 'FitMarginX': 0.0, 'FitMarginType': 0.0, 'FarZ': -1000.0, "
        "'FitMarginY': 0.0}}, 'PrevCtrlActiveColor': 4278190335.0, 'Viewer': "
        "{'EnableLUTs': False, 'LUTPlugin': 'FusionViewLUT', 'NearZ': 0.0, "
        "'FitMarginX': 0.0, 'FitMarginType': 0.0, 'FarZ': -1000.0, 'FitMarginY': "
        "0.0}, 'RulersShow': True}, 'View1': {'Viewer': {'EnableLUTs': False, "
        "'LUTPlugin': 'FusionViewLUT', 'NearZ': 0.0, 'FitMarginX': 0.0, "
        "'FitMarginType': 0.0, 'FarZ': -1000.0, 'FitMarginY': 0.0}, "
        "'PrevCtrlInactiveColor': 0.0, 'FullScreen': False, 'PrevCtrlActiveColor': "
        "0.0, 'PickH': 1.0, 'SideB': {'PrevCtrlInactiveColor': 4278255360.0, 'PickW': "
        "1.0, 'PickH': 1.0, 'PrevCtrlActiveColor': 4278190335.0, 'Viewer': "
        "{'EnableLUTs': False, 'LUTPlugin': 'FusionViewLUT', 'NearZ': 0.0, "
        "'FitMarginX': 0.0, 'FitMarginType': 0.0, 'FarZ': -1000.0, 'FitMarginY': "
        "0.0}}, 'AlwaysOnTop': True, 'PickW': 1.0}, 'Left': {'PrevCtrlInactiveColor': "
        "4278255360.0, 'PickW': 1.0, 'PickH': 1.0, 'SideB': {'PrevCtrlInactiveColor': "
        "4278255360.0, 'PickW': 1.0, 'PickH': 1.0, 'PrevCtrlActiveColor': "
        "4278190335.0, 'Viewer': {'EnableLUTs': False, 'LUTPlugin': 'FusionViewLUT', "
        "'NearZ': 0.0, 'FitMarginX': 0.0, 'FitMarginType': 0.0, 'FarZ': -1000.0, "
        "'FitMarginY': 0.0}}, 'PrevCtrlActiveColor': 4278190335.0, 'Viewer': "
        "{'EnableLUTs': False, 'LUTPlugin': 'FusionViewLUT', 'NearZ': 0.0, "
        "'FitMarginX': 0.0, 'FitMarginType': 0.0, 'FarZ': -1000.0, 'FitMarginY': "
        "0.0}, 'RulersShow': True}, 'View3D': {'FitToView': {'All': 1.0, 'Selected': "
        "0.75}, 'DefLight': {'Ambient': {'Intensity': 0.15}, 'Directional': "
        "{'Intensity': 0.85, 'Position': 0.0}}, 'Perspective': {'FovY': 45.0, "
        "'AdaptiveFar': False, 'StereoRigEye': 'Center', 'StereoMode': 'OffAxis', "
        "'Near': 0.05, 'EyeSeparation': 0.075, 'Far': 100000.0, 'AdaptiveNear': "
        "False, 'ConvergenceDistance': 2.5}, 'Orthographic': {'AdaptiveNear': False, "
        "'Near': -100000.0, 'Far': 100000.0, 'AdaptiveFar': False}, 'Grid': {'Minor': "
        "{'Enable': True, 'Width': 1.0, 'Color': 4283453520.0, 'Spacing': 0.25}, "
        "'Axes': {'Enable': True, 'Color': 4280492835.0, 'Width': 2.0}, 'Scale': 1.0, "
        "'Antialiasing': False, 'Major': {'Enable': True, 'Width': 1.0, 'Color': "
        "4280492835.0, 'Spacing': 2.0}, 'Size': 24.0}}, 'LeftView': {'PickW': 1.0, "
        "'PickH': 1.0}, 'RightView': {'PickW': 1.0, 'PickH': 1.0}}, "
        "'FreehandPrecDlg': {'Window': {'Left': 0.0, 'Top': 88.0}}, "
        "'FreehandLUTPrecDlg': {'Window': {'Left': 756.0, 'Top': 135.0}}, 'Cluster': "
        "{'SlaveClasses': 'all', 'SideFrames': 10.0, 'RenderRange': 1.0}, "
        "'QuickTime': {'DataCheck': True, 'KeyRate': 30.0, 'Compressor': 'Apple "
        "ProRes 422 LT_apcs', 'KeyCheck': True, 'DataRate': 1000.0, 'Quality': 90.0}, "
        "'DiskCache': {'NetGroups': 'all', 'CacheLoaders': {'DiskCache': True, "
        "'MultiFrame': True, 'Enable': True, 'Separator': '!', 'LimitedSize': False, "
        "'MaxSize': 200.0, 'OnMissingOrig': 0.0, 'NoLocal': False}}, 'LastLUTFile': "
        "'', 'Tweaks': {'CloneOverlayMethod': 0.0, 'DisableFlowReordering': False, "
        "'GPU': {'Enable': 1.0, 'Caching': 2.0}, 'CloneOverlayBlend': 0.6}}}")
    '''
    compPrefsFormat = compPrefs['Comp']['FrameFormat']
    name = compPrefsFormat['Name']
    height = compPrefsFormat['Height']
    width  = compPrefsFormat['Width']
    rate   = compPrefsFormat['Rate']
    print( f"             Config - name: {name}, height: {height}, width: {width}, rate: {rate}")


def main() :
    comp = fu.GetCurrentComp()
    comp.Stop()
    # comp.Lock()
    comp.StartUndo("Reporting")
    reportOnComp( comp )
    reportOnAllTools( comp )
    comp.EndUndo(True)
    # comp.Unlock()


if __name__ == "__main__" :
    main()
