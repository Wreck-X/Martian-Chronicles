from PySide6.QtWidgets import QRadioButton

class Curiositybutton(QRadioButton):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setText("Curiosity")