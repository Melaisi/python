'''
:author:
    Melaisi

:synopsis:
    This script contain the GUI elements of turntable tool for Maya

:description:
  Containt multiple options that will be used by turntable logic to create 
  a turntable camera render in Maya


'''
import sys
from PySide2 import QtCore, QtGui
from PySide2.QtWidgets import (
    QApplication,
    QMainWindow,
    QLayout,
    QDialog,
    QHBoxLayout,
    QVBoxLayout,
    QLabel,
    QPushButton,
    QLineEdit,
    QSlider,
    QWidget,
    
)

class SliderType:
    INT = 1
    DOUBLE = 2

class TurntableController(QtCore.QObject):
    selectionChanged = QtCore.Signal(list)


class TurntableWindow(QMainWindow):
    createClicked = QtCore.Signal([])


def create_window(controller,parent=None):
    window = TurntableWindow(parent)
    window.setWindowTitle("Turntable Camera")
    main_layout = QVBoxLayout()

    # Sliders
    distance = MySlider("Distance", SliderType.DOUBLE)
    height = MySlider("Height", SliderType.DOUBLE)
    degrees = MySlider("Degrees Per Frame", SliderType.DOUBLE)

    # Buttons
    create_button = QPushButton("Create turntable")


    main_layout.addLayout(distance.layout)
    main_layout.addLayout(height.layout)
    main_layout.addLayout(degrees.layout)
    
    main_layout.addWidget(create_button)
    

    central_container = QWidget(window)
    central_container.setLayout(main_layout)
    window.setCentralWidget(central_container)
    return window


class MySlider():
    def __init__(self,label,type):
        self.layout = QHBoxLayout()
        self.label = QLabel(label)
        
        self.input_line = QLineEdit()
        if(type == 1):
            self.validator = QtGui.QIntValidator()
        elif(type == 2):
             self.validator = QtGui.QDoubleValidator()
        else:
            self.validator = QtGui.QDoubleValidator()

        self.input_line.setValidator(self.validator)        
        self.slider = QSlider(QtCore.Qt.Horizontal)

        self.layout.addWidget(self.label)
        self.layout.addWidget(self.input_line)
        self.layout.addWidget(self.slider)

