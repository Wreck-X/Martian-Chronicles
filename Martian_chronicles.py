import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget ,QHBoxLayout,QLineEdit,QCalendarWidget,QStackedWidget,QComboBox
from buttons import *
from PySide6.QtCore import Qt,QThread, Signal
class MainWindow(QMainWindow):
    
    def __init__(self,parent=None):
        super().__init__(parent)
        mainlayout = QHBoxLayout()
        buttonlayout = QVBoxLayout()
        imagelayout = QVBoxLayout()
        stacked_widget = QStackedWidget()
        self.combobox = QComboBox
        self.calendar = QCalendarWidget()
        self.calendar.setFixedSize(180,180)
        self.line_edit = QLineEdit(self)
        self.line_edit.setFixedSize(180,25)
        button1 = Button1(stacked_widget)
        button2 = Button2(stacked_widget)
        button3 = Button3(self.line_edit)
        button4 = Fetchbutton(mainlayout,imagelayout,stacked_widget,self.calendar)
        rb1 = Curiosity()
        rb2 = Opportunity()
        rb3 = Spirit()
        buttonlayout.addWidget(button1)
        buttonlayout.addWidget(button2)
        buttonlayout.addWidget(button4)
        buttonlayout.addWidget(rb1)
        buttonlayout.addWidget(rb2)
        buttonlayout.addWidget(rb3)
        buttonlayout.addWidget(self.calendar)
        buttonlayout.addWidget(self.line_edit)
        buttonlayout.addWidget(button3)
        buttonlayout.setAlignment(Qt.AlignLeft)
        mainlayout.addLayout(buttonlayout)
        central_widget = QWidget()
        central_widget.setLayout(mainlayout)
        self.setCentralWidget(central_widget)
        self.setGeometry(100, 100, 800, 600)
    def taketext(self):
        global textval
        textval = self.line_edit.text()
        print(textval)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          
if __name__ == '__main__':
    app = QApplication(sys.argv)                                
    window = MainWindow()
    window.show()
    sys.exit(app.exec())