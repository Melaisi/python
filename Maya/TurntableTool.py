#For getting maya main window 
from PySide2.QtWidgets import QMainWindow
from shiboken2 import wrapInstance
import maya._OpenMayaUI as OpenMayaUI

import TurntableGUI 
_window = None
def show():
    global _window
    if _window is None:
        controller = TurntableGUI.TurntableController()
        parent = get_maya_window()
        _window = TurntableGUI.create_window(controller,parent)
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
