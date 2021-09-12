'''
Resource https://www.pythonguis.com/tutorials/creating-your-first-pyqt-window/
'''

import sys
import PySide2
from PySide2 import QtCore
from PySide2.QtCore import QLine
from PySide2.QtWidgets import (
    QAction,
    QApplication, 
    QCheckBox,
    QComboBox,
    QDateEdit,
    QDial,
    QDialog,
    QDoubleSpinBox,
    QFontComboBox,
    QHBoxLayout,
    QLabel,
    QLCDNumber, 
    QLineEdit,
    QMainWindow,
    QProgressBar, 
    QPushButton, 
    QSlider,
    QSpinBox,
    QTimeEdit,
    QVBoxLayout,
    QWidget,
)

from PySide2.QtGui import QDoubleValidator, QIntValidator, QPalette,QColor

class MySlider():
    def __init__(self,label,type):
        self.widgets = []
        
        self.label = QLabel(label)
        
        self.input_line = QLineEdit()
        if(type == 1):
            self.double_validator = QIntValidator()
        elif(type == 2):
             self.double_validator = QDoubleValidator()
        else:
            self.double_validator = QDoubleValidator()

        self.input_line.setValidator(self.double_validator)        
        self.slider = QSlider(QtCore.Qt.Horizontal)
        
        self.widgets.append(self.label)
        self.widgets.append(self.input_line)
        self.widgets.append(self.slider)

class Color(QWidget):
    def __init__(self, color):
        super(Color,self).__init__()

        self.setAutoFillBackground(True)
        pallette = self.palette()
        pallette.setColor(QPalette.Window,QColor(color))
        self.setPalette(pallette)



class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow,self).__init__()
        self.setWindowTitle("Hello Layout")
        
        layout1 = QHBoxLayout()
        layout2 = QVBoxLayout()
        layout3 = QVBoxLayout()

        layout2.addWidget(Color('red'))
        layout2.addWidget(Color('yellow'))
        layout2.addWidget(Color('purple'))

        layout1.addLayout(layout2)

        layout1.addWidget(Color('green'))

        layout3.addWidget(Color('red'))
        layout3.addWidget(Color('purple'))

        layout1.addLayout(layout3)



        widget = QWidget()
        widget.setLayout(layout1)

        self.setCentralWidget(widget)

        #MENU 
        about_action = QAction("&About",self)
        about_action.triggered.connect(self.onAboutClick)
        about_action.setCheckable(True)
        menu = self.menuBar()
        help_menu = menu.addMenu("&Help")
        help_menu.addAction(about_action)
        

    
    def onAboutClick(self,s):
        dialog = QDialog(self)
        dialog.setWindowTitle("About Turntable camera tool")
        dialog.exec_()


        



app = QApplication(sys.argv)
#Create Buttons Slots  

window = MainWindow()
window.show()

app.exec_()