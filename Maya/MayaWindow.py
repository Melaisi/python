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

# import sys, needed for QtWidgets.QApplication instance
import sys

class HelloWindow(QtWidgets.QMainWindow):
    createClicked = Signal(str)

def create_window():
    window = HelloWindow()
    window.setWindowTitle('Hello Maya')

    container = QtWidgets.QWidget(window)
    
    label = QtWidgets.QLabel('Distance', container)
    textbox = QtWidgets.QLineEdit(container)

    create_button = QtWidgets.QPushButton("Create",container)
    cancel_button = QtWidgets.QPushButton("Cancel",container)

    def onClick():
        window.createClicked.emit(textbox.text())
    create_button.clicked.connect(onClick)

    layout = QtWidgets.QHBoxLayout(container)
    container.setLayout(layout)
    # Add widget to layout 
    layout.addWidget(label)
    layout.addWidget(textbox)
    layout.addWidget(create_button)
    layout.addWidget(cancel_button)
    

    window.setCentralWidget(container)

    return window

if __name__ == '__main__':
    def oncreate(text):
        print("Create Clicked, text is:",text)

    if not QtWidgets.QApplication.instance():
        app = QtWidgets.QApplication(sys.argv)
    else:
        app = QtWidgets.QApplication.instance()
    win = create_window()
    win.createClicked.connect(oncreate)
    win.show()
    sys.exit(app.exec_())