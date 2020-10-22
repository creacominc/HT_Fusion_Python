#!/usr/bin/env python3

from pprint import pprint

comp = fu.GetCurrentComp()

def dialogTest() :
    # example dialog
    # In Python make sure to create a dictionary with proper indices starting with 1
    dialog = {
        1: {
            1: "dlgDir",
            "Name": "Select a Directory",
            2: "PathBrowse"
        },
        2: {
            1: "dlgCheck",
            "Name": "A Check Box",
            2: "Checkbox",
            "Default": 1
        }
    }
    ret = composition.AskUser("A sample dialog", dialog)
    pprint( ret )

def undoTest() :
    # demo of ability to undo as a group.
    comp.StartUndo("Add some tools")
    bg1 = comp.Background()
    pl1 = comp.Plasma()
    mg1 = comp.Merge({ "Background": bg1, "Foreground": pl1 })
    comp.EndUndo(True)

def findToolsTest() :
    # finding tools
    # Create three Blur tools
    blur1 = comp.Blur()
    blur2 = comp.Blur()
    blur3 = comp.Blur()
    print (comp.FindToolByID("Blur").Name)
    # Prints: Blur1
    print (comp.FindToolByID("Blur", blur1).Name)
    # Prints: Blur2
    print (comp.FindToolByID("Blur", blur2).Name)
    # Prints: Blur3
    #print (comp.FindToolByID("Blur", blur3).Name) - blur3 does not have a blur child.
    pprint( blur3.Name )

def testPrefs() :
    # All but default preferences
    pprint(comp.GetPrefs(None, False))

def listAllTools() :
    # outputs the name of every tool in the composition
    #pprint(comp.GetToolList())
    # print all tool names and ids
    for tool in comp.GetToolList().values() :
        pprint( f'Tool ID: {tool.ID},  Name: {tool.Name}' )
        children = tool.GetChildrenList().values()
        if( children ) :
            pprint( f'     Children of {tool.Name}')
            for child in children :
                # pprint( child )
                pprint( f'     child ID: {child.ID},  Name: {child.Name}' )

def listSelectedTools() :
    # Get all selected tools
    pprint(comp.GetToolList(True))
    # Get all loaders
    pprint(comp.GetToolList(False, "Loader"))


def doTesting() :
    ### Prevent updating from here to the end
    comp.Lock()

    # change format on all nodes
    compName = comp.Name
    pprint( f"Name: {compName}" )

    ### Allow updating from here to the end
    comp.Unlock()


def main() :
    compPrefsFormat = comp.GetPrefs()['Comp']['FrameFormat']

    name = compPrefsFormat['Name']
    height = compPrefsFormat['Height']
    width  = compPrefsFormat['Width']
    rate   = compPrefsFormat['Rate']

    print( f"Current config - name: {name}, height: {height}, width: {width}, rate: {rate}")

    #dialogTest()
    #undoTest()
    #findToolsTest()
    #testPrefs()
    listAllTools()
    #listSelectedTools()

if __name__ == "__main__" :
    main()
