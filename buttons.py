from PySide6.QtWidgets import  QPushButton,QRadioButton,QWidget,QLabel,QComboBox
from PySide6.QtGui import QPixmap
import threading
import requests,os,json,ezgmail
os.chdir(r'/home/wreck/Desktop/Projects/Martian-Chronicles/')
marskey = os.getenv("marskey")
rovername = ""
count = None
earth_date = ""
maxcount = 24

class Button1(QPushButton):
    def __init__(self, stacked_widget):
        super().__init__(parent=None)
        self.setText("Next Image")
        self.clicked.connect(self.showMessage)
        self.setFixedSize(200,50)
        self.stacked_widget = stacked_widget
    def showMessage(self):
        global count
        if count == None:
            count = 1
        else:
            if count<maxcount:
                count+= 1
            else:
                count = 0
        print(count)
        self.stacked_widget.setCurrentIndex(count)


class Button2(QPushButton):
    def __init__(self,stacked_widget):
        super().__init__()
        self.setText("Previous Image")
        self.clicked.connect(self.showMessage)
        self.setFixedSize(200,50)
        self.stacked_widget = stacked_widget
    def showMessage(self):
        global count
        if count == None:
            count = maxcount
        else:
            if count>0:
                count -= 1
            else:
                count = maxcount
        print(count)
        self.stacked_widget.setCurrentIndex(count)
        

class Button3(QPushButton):

    def __init__(self, linedit):
        super().__init__()
        self.setText("Send Email")
        self.setFixedSize(200,50)
        self.clicked.connect(self.threading)
        self.linedit = linedit
        
    def showMessage(self):
        pnglist = [f"{i}.png" for i in range(maxcount + 1)]
        print(pnglist)
        mail = self.linedit.text().split(',')
        for i in mail:
            ezgmail.send(i,'lmao','idk',pnglist)
            print("sent email to ",i)

    def threading(self):
        thread = threading.Thread(target=self.showMessage)
        thread.start()
class Fetchbutton(QPushButton):
    def __init__ (self,mainlayout,imagelayout,stacked_widget,calendar):
        super().__init__()
        self.setText("Fetch")
        self.setFixedSize(95,50)
        self.calender = calendar
        self.imagelayout = imagelayout
        self.stacked_widget = stacked_widget
        self.mainlayout = mainlayout
        self.clicked.connect(self.threading)
        
    
    def fetchdata(self):
        global maxcount
        earth_date  = self.calender.selectedDate().toString()
        earth_date = earth_date.split()
        earth_date.pop(0)
        monthdict = {"Jan":"1","Feb":"2","Mar":"3","Apr":"4","May":"5","Jun":"6","Jul":"7","Aug":"8","Sep":"9","Oct":"10","Nov":"11","Dec":"12"}
        earth_date[0] = monthdict[earth_date[0]]
        month = earth_date[0]
        day = earth_date[1]
        year = earth_date[2]
        earth_date = year + "-" + month + "-" + day
        print(f"https://api.nasa.gov/mars-photos/api/v1/rovers/{rovername}/photos?earth_date={earth_date}&api_key={marskey}")
        json_data = requests.get(f"https://api.nasa.gov/mars-photos/api/v1/rovers/{rovername}/photos?earth_date={earth_date}&api_key={marskey}").json()
        print(json.dumps(json_data,indent= 3))
        urlist = []
        for i in range(25):
            try:
                urlist.append(json_data["photos"][i]["img_src"])
            except IndexError:
                maxcount = i
                break
        for index,item in enumerate(urlist):
            response = requests.get(item,allow_redirects=True)
            if response.status_code:
                open(f"{index}.png",'wb').write(response.content)



    def threading(self):
        thread = threading.Thread(target=self.fetchdata)
        thread.start()



class ShowButton(QPushButton):
    def __init__ (self,stacked_widget,imagelayout,mainlayout):
        super().__init__()
        self.setText("Show")
        self.setFixedSize(95,50)
        self.clicked.connect(self.showImage)
        self.stacked_widget = stacked_widget
        self.imagelayout = imagelayout
        self.mainlayout = mainlayout
    def showImage(self):
        for i in range(25):
            label = QLabel()
            pixmap = QPixmap(f"{i}.png").scaled(500,480)
            label.setPixmap(pixmap)
            self.stacked_widget.addWidget(label)
        self.stacked_widget.setCurrentIndex(0)
        self.imagelayout.addWidget(self.stacked_widget)
        self.mainlayout.addLayout(self.imagelayout)       


class Curiosity(QWidget):
    def __init__(self):
        super().__init__()
        self.resize(50, 250)
        self.radio = QRadioButton("Curiosity", self)
        self.radio.toggled.connect(self.ischecked)    
    def ischecked(self, checked):
        global rovername
        if checked:
            rovername = 'Curiosity'
            print(rovername)
 
class Opportunity(QWidget):
    def __init__(self):
        super().__init__()
        self.resize(50, 250)
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
        self.resize(50, 250)
        self.radio = QRadioButton("Spirit", self)
        self.radio.toggled.connect(self.ischecked)   
    def ischecked(self, checked):
        global rovername
        if checked:
            rovername = 'Spirit'
            print(rovername)
            
class Roverlist(QComboBox):
    def __init__(self):
        super().__init__()
        self.addItems(["Curiosity","Opportunity","Spirit"])
        self.currentIndexChanged.connect(self.indexchanged)

    def indexchanged(self,index):
        global rovername
        if index == 0:
            rovername = "curiosity"
        if index == 1:
            rovername = "opportunity"
        if index == 2:
            rovername = "spirit"

# class CloneThread(QThread):
#     signal = Signal('PyQt_PyObject')

#     def __init__(self):
#         QThread.__init__(self)
#         self.git_url = ""

#     # run method gets called when we start the thread
#     def run(self):
#         tmpdir = tempfile.mkdtemp()
#         cmd = "git clone {0} {1}".format(self.git_url, tmpdir)
#         subprocess.check_output(cmd.split())
#         # git clone done, now inform the main thread with the output
#         self.signal.emit(tmpdir)