import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QLabel, QGridLayout, QWidget
from PySide6.QtGui import QPixmap

class Image(QLabel):

    def __init__(self, image_path):
        super().__init__()
        pixmap = QPixmap(image_path)
        self.setPixmap(pixmap.scaled(400,400))
