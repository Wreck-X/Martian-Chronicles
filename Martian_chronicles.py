import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget ,QHBoxLayout, QGridLayout ,QButtonGroup,QLineEdit
from PySide6.QtGui import QPixmap
from buttons import *
from image import *

class MainWindow(QMainWindow):
    
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        mainlayout = QHBoxLayout()
        buttonlayout = QVBoxLayout()
        lineedit = LineEdit()
        button1 = Button1(mainlayout)
        button2 = Button2(mainlayout)
        button3 = Button3(self)
        button4 = Fetchbutton(lineedit)
        rb1 = Curiosity()
        rb2 = Opportunity()
        rb3 = Spirit()
        
        buttonlayout.addWidget(button1)
        buttonlayout.addWidget(button2)
        buttonlayout.addWidget(button3)
        buttonlayout.addWidget(button4)
        buttonlayout.addWidget(rb1)
        buttonlayout.addWidget(rb2)
        buttonlayout.addWidget(rb3)
        buttonlayout.addWidget(lineedit)
        mainlayout.addLayout(buttonlayout)
        central_widget = QWidget()
        central_widget.setLayout(mainlayout)
        self.setCentralWidget(central_widget)
        self.setGeometry(100, 100, 600, 400)
        
if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())