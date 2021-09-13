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
    QPushButton,
    QLineEdit,
    QSlider,
    QWidget,
    
)

class TurntableController(QtCore.QObject):
    selectionChanged = QtCore.Signal(list)


class TurntableWindow(QMainWindow):
    createClicked = QtCore.Signal([])


def create_window(controller,parent=None):
    window = TurntableWindow(parent)
    window.setWindowTitle("Turntable Camera")
    central_container = QWidget(window)
    window.setCentralWidget(central_container)
    return window

