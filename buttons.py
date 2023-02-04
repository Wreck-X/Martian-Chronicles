from PySide6.QtWidgets import  QPushButton
import requests,os

marskey = os.getenv("marskey")
rovername = "Curiosity"
earth_date = "earth_date=2015-6-3&"
class Button1(QPushButton):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setText("Button 1")
        self.clicked.connect(self.showMessage)
        self.setFixedSize(100,50)
    def showMessage(self):
        print("Button 1 was clicked")

class Button2(QPushButton):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setText("Button 2")
        self.clicked.connect(self.showMessage)
        self.setFixedSize(100,50)
    def showMessage(self):
        print("Button 2 was clicked")

class Button3(QPushButton):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setText("Button 3")
        self.setFixedSize(100,50)
        self.clicked.connect(self.showMessage)
        
    def showMessage(self):
        print("Button 3 was clicked")

class Fetchbutton(QPushButton):
    def __init__ (self, parent=None):
        super().__init__(parent)
        self.setText("Fetch Image")
        self.setFixedSize(100,50)
        self.clicked.connect(self.fetchdata)
    
    def fetchdata(self):
        json_data = requests.get(f"https://api.nasa.gov/mars-photos/api/v1/rovers/{rovername}/latest_photos?{earth_date}api_key={marskey}").json()
        print(json_data)