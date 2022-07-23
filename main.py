
from time import sleep
import sys


import pygame

# from PySide6 import QtWidgets, QtCore
from PySide6.QtWidgets import *
from PySide6.QtCore import *

from ui_main import Ui_MainWindow


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.guidLabel.setText("controller guid:\n" + getController()[0].get_guid())
        self.ui.testButton.clicked.connect(testVibrate)

@Slot()
def testVibrate():
    controller = getController()[0]
    controller.rumble(False, True, 0)
    sleep(1)
    controller.stop_rumble()

# @Slot()
# def startVibrate():
    
#     pass

# def getDuration():
    

def getController():
    return [pygame.joystick.Joystick(x) for x in range(pygame.joystick.get_count())]

# def detectControllers():
#     return controllerList[0].get_guid()


if __name__ == '__main__':
    pygame.joystick.init()
    
    app = QApplication(sys.argv)
    
    window = MainWindow()
    window.show()
    
    
    # window.label.setText(detectControllers())
    
    sys.exit(app.exec())


# for i in range(5):
#     controller.rumble(False, True, 0)
#     sleep(1)
#     controller.stop_rumble()
#     sleep(.2)
#     # sleep()