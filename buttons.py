from PySide6.QtWidgets import  QPushButton,QVBoxLayout,QRadioButton,QLineEdit
import requests,os,json
from image import *
from Martian_chronicles import *
marskey = os.getenv("marskey")
rovername = ""
earth_date = "earth_date=2015-6-3&"
count = None
class Button1(QPushButton):
    def __init__(self, mainlayout, *args, **kwargs):
        super().__init__(*args,**kwargs)
        self.setText("Next Image")
        self.clicked.connect(self.showMessage)
        self.setFixedSize(120,50)
        self.mainlayout = mainlayout
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
        if self.mainlayout.count() == 1:
            imagelayout = QVBoxLayout()
            image = Image(f"./{count}.png")     
            imagelayout.addWidget(image)
            self.mainlayout.addLayout(imagelayout)
        else:
            im = self.mainlayout.takeAt(1)
            try:
                im.pop()
            except AttributeError:
                pass


class Button2(QPushButton):
    def __init__(self, mainlayout, *args, **kwargs):
        super().__init__(*args,**kwargs)
        self.setText("Previous Image")
        self.clicked.connect(self.showMessage)
        self.setFixedSize(120,50)
        self.mainlayout = mainlayout
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
        if self.mainlayout.count() == 1:
            imagelayout = QVBoxLayout()
            image = Image(f"./{count}.png")     
            imagelayout.addWidget(image)
            self.mainlayout.addLayout(imagelayout)
        else:
            im = self.mainlayout.takeAt(1)
            try:
                im.pop()
            except AttributeError:
                pass

class Button3(QPushButton):

    def __init__(self, parent=None):
        super().__init__(parent)
        self.setText("Button 3")
        self.setFixedSize(120,50)
        self.clicked.connect(self.showMessage)
        
    def showMessage(self):
        print("Button 3 was clicked")

class Fetchbutton(QPushButton):
    def __init__ (self):
        super().__init__()
        self.setText("Fetch Image")
        self.setFixedSize(120,50)

        self.clicked.connect(self.fetchdata)
    
    def fetchdata(self):
        print(self.lineedit.text())
        print(f"https://api.nasa.gov/mars-photos/api/v1/rovers/{rovername}/latest_photos?{earth_date}api_key={marskey}")
        # json_data = requests.get(f"https://api.nasa.gov/mars-photos/api/v1/rovers/{rovername}/latest_photos?{earth_date}api_key={marskey}").json()
        # print(json.dumps(json_data,indent= 3))
        # urlist = []
        # for i in range(25):
        #     try:
        #         urlist.append(json_data["latest_photos"][i]["img_src"])
        #     except IndexError:
        #         break
        # for index,item in enumerate(urlist):
        #     response = requests.get(item,allow_redirects=True)
        #     if response.status_code:
        #         open(f"{index}.png",'wb').write(response.content)

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
        global rovername
        if checked:
            rovername = 'Spirit'
            
class LineEdit(QWidget):
    def __init__(self):
        super().__init__()        
