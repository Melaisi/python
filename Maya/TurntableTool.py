#For getting maya main window 
from PySide2.QtWidgets import QMainWindow
from shiboken2 import wrapInstance
import maya._OpenMayaUI as OpenMayaUI
import maya.cmds as cmds

import TurntableGUI 
_window = None
def show():
    global _window
    if _window is None:
        
        parent = get_maya_window()
        _window = TurntableGUI.create_window(parent)
        def onCreate(args):
            create_turntable(args)
        _window.createClicked.connect(onCreate)
    _window.show()

def get_maya_window():
    """Return the QMainWindow for the main Maya window """
    """Source: practical maya programming book"""
    winptr = OpenMayaUI.MQtUtil_mainWindow()
    if winptr is None:
        raise RuntimeError(winptr)
    window = wrapInstance(long(winptr),QMainWindow)
    assert isinstance(window,QMainWindow)
    return window

def create_turntable(args):
    # get the selected objects
    selected = cmds.ls(sl=True,long=True) 
    # Todo: check if empty display error message 
    if not selected:
        print("Please select an object")
        return 
    # get the world space center of the objects bounding box
    #  
    

    
