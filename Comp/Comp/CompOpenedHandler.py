#!/usr/bin/env python3

def loadFirstSaverToViewer2( comp ) :
    comp.StartUndo("LoadSaverToViewer2")
    comp.Stop()
    comp.Lock()
    # find first saver
    for tool in comp.GetToolList(False, "Saver").values() :
        print( '' )
        print( f'Loading Saver to View 2.  Id: {tool.ID},  Name: {tool.Name}' )
        # Select and show this tool in window 2
        comp.SetActiveTool( tool )
        comp.CurrentFrame.ViewOn( tool, 2 )
    comp.Unlock()
    comp.EndUndo(True)


def main() :
    comp = fu.GetCurrentComp()
    loadFirstSaverToViewer2( comp )

if __name__ == "__main__" :
    main()
