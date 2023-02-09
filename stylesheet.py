style = '''
QPushButton { background-color: #454545; border-style: outset; padding: 6px; border-width: 2px; border-radius: 10px; border-color: beige; color : white;}

QComboBox {
    border: 1px solid gray;
    border-radius: 3px;
    padding: 1px 18px 1px 3px;
    min-width: 6em;
}

QComboBox:editable {
    background: white;
}

QComboBox:!editable, QComboBox::drop-down:editable {
     background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,
                                 stop: 0 #E1E1E1, stop: 0.4 #DDDDDD,
                                 stop: 0.5 #D8D8D8, stop: 1.0 #D3D3D3);
}


QComboBox:!editable:on, QComboBox::drop-down:editable:on {
    background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,
                                stop: 0 #D3D3D3, stop: 0.4 #D8D8D8,
                                stop: 0.5 #DDDDDD, stop: 1.0 #E1E1E1);
}

QComboBox:on {
    padding-top: 3px;
    padding-left: 4px;
}

QComboBox::drop-down {
    subcontrol-origin: padding;
    subcontrol-position: top right;
    width: 15px;

    border-left-width: 1px;
    border-left-color: darkgray;
    border-left-style: solid; 
    border-top-right-radius: 3px; 
    border-bottom-right-radius: 3px;
}

QComboBox::down-arrow {
    image: url(/usr/share/icons/crystalsvg/16x16/actions/1downarrow.png);
}

QComboBox::down-arrow:on {
    top: 1px;
    left: 1px;
}

QLineEdit { background-color: #454545}

QCalendarWidget QToolButton {
  	color: white;
  	background-color: qlineargradient(x1:0, y1:0, x2:0, y2:1, stop: 0 #cccccc, stop: 1 #333333);
  }
  QCalendarWidget QMenu {
  	left: 20px;
  	color: white;
  	font-size: 18px;
  	background-color: rgb(100, 100, 100);
  }
  QCalendarWidget QSpinBox { 
  	color: white; 
  	background-color: qlineargradient(x1:0, y1:0, x2:0, y2:1, stop: 0 #cccccc, stop: 1 #333333); 
  	selection-background-color: rgb(136, 136, 136);
  	selection-color: rgb(255, 255, 255);
  }
  QCalendarWidget QSpinBox::up-button { subcontrol-origin: border;  subcontrol-position: top right; }
  QCalendarWidget QSpinBox::down-button {subcontrol-origin: border; subcontrol-position: bottom right; }

   

  QCalendarWidget QWidget { alternate-background-color: rgb(128, 128, 128); }

  QCalendarWidget QAbstractItemView:enabled 
  {
  	color: rgb(180, 180, 180);  
  	background-color: black;  
  	selection-background-color: rgb(64, 64, 64); 
  	selection-color: rgb(0, 255, 0); 
  }
   
QCalendarWidget QWidget#qt_calendar_navigationbar
{ 
  background-color: qlineargradient(x1:0, y1:0, x2:0, y2:1, stop: 0 #cccccc, stop: 1 #333333); 
}

QCalendarWidget QAbstractItemView:disabled 
{ 
color: rgb(64, 64, 64); 
}

QMainWindow#mainwindow {
    background-color: #272727
}
'''