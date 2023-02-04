import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget ,QHBoxLayout
from buttons import *
from radiobuttons import *
class MainWindow(QMainWindow):

    def __init__(self, parent=None):
        super().__init__(parent)

        button1 = Button1(self)
        button2 = Button2(self)
        button3 = Button3(self)
        button4 = Fetchbutton(self)
        
        buttonlayout = QVBoxLayout()
        buttonlayout.addWidget(button1)
        buttonlayout.addWidget(button2)
        buttonlayout.addWidget(button3)
        buttonlayout.addWidget(button4)
        
        radbutt1 = Curiositybutton()
        radbuttonlayout = QHBoxLayout()
        radbuttonlayout.addWidget(radbutt1)

        # central_widget = QWidget()
        # central_widget.setLayout(buttonlayout)

        radbutt_widget = QWidget()
        radbutt_widget.setLayout(radbuttonlayout)
        # self.setCentralWidget(central_widget)
        self.setGeometry(100, 100, 600, 400)
        
if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())