import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget ,QHBoxLayout,QLineEdit,QCalendarWidget,QStackedWidget
from buttons import *
from PySide6.QtCore import Qt
from stylesheet import *
class MainWindow(QMainWindow):
    
    def __init__(self,parent=None):
        super().__init__(parent)
        mainlayout = QHBoxLayout()
        buttonlayout = QVBoxLayout()
        subbuttonlayout = QHBoxLayout()
        imagelayout = QVBoxLayout()
        stacked_widget = QStackedWidget()
        combobox = Roverlist()

        self.calendar = QCalendarWidget()
        self.calendar.setFixedSize(200,200)
        self.line_edit = QLineEdit(self)
        self.line_edit.setFixedSize(200,25)
        self.line_edit.setStyleSheet("background-color: #737373; color: white")
        button1 = Button1(stacked_widget)
        button2 = Button2(stacked_widget)
        button3 = Button3(self.line_edit)
        button4 = Fetchbutton(mainlayout,imagelayout,stacked_widget,self.calendar)
        button5 = ShowButton(stacked_widget,imagelayout,mainlayout)
        buttonlayout.addWidget(button1)
        buttonlayout.addWidget(button2)
        subbuttonlayout.addWidget(button4)
        subbuttonlayout.addWidget(button5)
        buttonlayout.addLayout(subbuttonlayout)
        buttonlayout.addWidget(combobox)
        buttonlayout.addWidget(self.calendar)
        buttonlayout.addWidget(self.line_edit)
        buttonlayout.addWidget(button3)
        buttonlayout.setAlignment(Qt.AlignLeft)
        mainlayout.addLayout(buttonlayout)
        central_widget = QWidget()
        central_widget.setLayout(mainlayout)
        self.setCentralWidget(central_widget)
        self.setFixedSize(700, 500)
        self.setObjectName("mainwindow")
        self.setWindowTitle("Martian-Chronicles")
    def taketext(self):
        global textval
        textval = self.line_edit.text()
        print(textval)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          
if __name__ == '__main__':
    app = QApplication(sys.argv)  
    app.setStyleSheet(style)                         
    window = MainWindow()
    window.show()
    sys.exit(app.exec())