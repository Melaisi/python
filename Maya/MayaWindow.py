'''
The goal of this script to display a non funcitonal user interface with elements 
to create turntable with multiple options.

This file hosted in external directory using userSetup.py  

Resourcces:
   Practical Maya Programming with Python - Galanakis, Robert, 
    Chapter 5. Building Graphical User Interfaces for Maya

Basic Required UI elements:
    1) Create Button 
    2) Cancel Button 
    3) Distance Slider  
    4) Distance Text Input field  
    5) Height Slider
    6) Height Text Input field 
    7) Angle per frame Text Input field [Speed]
'''

# import Qt related module 
from PySide2 import QtCore, QtGui, QtWidgets 
Signal = QtCore.Signal

def create_window():
    win = QtWidgets.QMainWindow()
    return win


def display_window():
    # From https://stackoverflow.com/a/63708668/11358872 
    if not QtWidgets.QApplication.instance():
        app = QtWidgets.QApplication(sys.argv)
    else:
        app = QtWidgets.QApplication.instance()
    win = create_window()
    win.show()
    app.exec_()