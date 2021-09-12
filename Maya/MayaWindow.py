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
    window.setWindowTitle('Hello Qt Widgets')

    container = QtWidgets.QWidget(window)
    
    # Distance (from object ? origin? )
    
    distance_label = QtWidgets.QLabel('Distance')
    distance_input = QtWidgets.QLineEdit()
    distance_slider = QtWidgets.QSlider(QtCore.Qt.Horizontal)

    # Height ( current object Y + new height ? or from origin )

    height_label = QtWidgets.QLabel('Height')
    height_input = QtWidgets.QLineEdit()
    height_slider = QtWidgets.QSlider(QtCore.Qt.Horizontal)

    # Speed (Degrees per Frame)
    speed_label = QtWidgets.QLabel("Degrees per frame")
    speed_input = QtWidgets.QLineEdit()
    speed_slider = QtWidgets.QSlider(QtCore.Qt.Horizontal)

    # Frames ( How many frames ) ?

    create_button = QtWidgets.QPushButton("Create",container)
    cancel_button = QtWidgets.QPushButton("Cancel",container)

    def onClick():
        window.createClicked.emit("Crete Clicked")
    create_button.clicked.connect(onClick)

    layout = QtWidgets.QHBoxLayout(container)
    container.setLayout(layout)
    # Add widget to layout 
    

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