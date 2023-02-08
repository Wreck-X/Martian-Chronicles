from PySide6.QtWidgets import  QPushButton,QVBoxLayout,QRadioButton,QLineEdit,QStackedWidget,QWidget,QLabel
from PySide6.QtGui import QPixmap
import requests,os,json
import Martian_chronicles
marskey = os.getenv("marskey")
rovername = ""
count = None
earth_date = ""
class Button1(QPushButton):
    def __init__(self, stacked_widget):
        super().__init__()
        self.setText("Next Image")
        self.clicked.connect(self.showMessage)
        self.setFixedSize(120,50)
        self.stacked_widget = stacked_widget
    def showMessage(self):
        global count
        if count == None:
            count = 0
        else:
            if count<24:
                count+= 1
            else:
                count = 0
        print(count)
        self.stacked_widget.setCurrentIndex(count)
        # if self.mainlayout.count() == 1:
        #     imagelayout = QVBoxLayout()
        #     image = Image(f"./{count}.png")     
        #     imagelayout.addWidget(image)
        #     self.mainlayout.addLayout(imagelayout)
        # else:
        #     im = self.mainlayout.takeAt(1)
        #     try:
        #         im.pop()
        #     except AttributeError:
        #         pass


class Button2(QPushButton):
    def __init__(self,stacked_widget):
        super().__init__()
        self.setText("Previous Image")
        self.clicked.connect(self.showMessage)
        self.setFixedSize(120,50)
        self.stacked_widget = stacked_widget
    def showMessage(self):
        global count
        if count == None:
            count = 24
        else:
            if count>0:
                count -= 1
            else:
                count = 24
        print(count)
        self.stacked_widget.setCurrentIndex(count)
        

class Button3(QPushButton):

    def __init__(self, parent=None):
        super().__init__(parent)
        self.setText("Button 3")
        self.setFixedSize(120,50)
        self.clicked.connect(self.showMessage)
        
    def showMessage(self):
        print("Button 3 was clicked")

class Fetchbutton(QPushButton):
    def __init__ (self,linedit,mainlayout,imagelayout,stacked_widget):
        super().__init__()
        self.setText("Fetch Image")
        self.setFixedSize(120,50)
        self.line_edit = linedit
        self.imagelayout = imagelayout
        self.stacked_widget = stacked_widget
        self.mainlayout = mainlayout
        self.clicked.connect(self.fetchdata)
        
    
    def fetchdata(self):
        # global earth_date
        # earth_date = "earth_date="+self.line_edit.text()+"&"
        # print(f"https://api.nasa.gov/mars-photos/api/v1/rovers/{rovername}/photos?{earth_date}api_key={marskey}")
        # json_data = requests.get(f"https://api.nasa.gov/mars-photos/api/v1/rovers/{rovername}/photos?{earth_date}api_key={marskey}").json()
        # print(json.dumps(json_data,indent= 3))
        # urlist = []
        # for i in range(25):
        #     try:
        #         urlist.append(json_data["photos"][i]["img_src"])
        #     except IndexError:
        #         break
        # for index,item in enumerate(urlist):
        #     response = requests.get(item,allow_redirects=True)
        #     if response.status_code:
        #         open(f"{index}.png",'wb').write(response.content)

        for i in range(25):
            label = QLabel()
            pixmap = QPixmap(f"{i}.png").scaled(400,400)
            label.setPixmap(pixmap)
            self.stacked_widget.addWidget(label)
        self.stacked_widget.setCurrentIndex(0)
        self.imagelayout.addWidget(self.stacked_widget)
        self.mainlayout.addLayout(self.imagelayout)

class Curiosity(QWidget):
    def __init__(self):
        super().__init__()
        self.resize(300, 250)
        self.radio = QRadioButton("Curiosity", self)
        self.radio.toggled.connect(self.ischecked)    
    def ischecked(self, checked):
        global rovername
        if checked:
            rovername = 'Curiosity'
 
class Opportunity(QWidget):
    def __init__(self):
        super().__init__()
        self.resize(300, 250)
        self.radio = QRadioButton("Opportunity", self)
        self.radio.toggled.connect(self.ischecked)   
    def ischecked(self, checked):
        global rovername
        if checked:
            rovername = 'Opportunity'
        print(rovername)

class Spirit(QWidget):
    def __init__(self):
        super().__init__()
        self.resize(300, 250)
        self.radio = QRadioButton("Spirit", self)
        self.radio.toggled.connect(self.ischecked)   
    def ischecked(self, checked):
        if checked:
            self.rovername = 'Spirit'
            
class LineEdit(QLineEdit):
    def __init__(self,parent=None):
        super().__init__()        
        self.setFixedSize(120,25)
