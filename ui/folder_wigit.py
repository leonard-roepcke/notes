from PyQt5.QtWidgets import QWidget, QVBoxLayout, QTextEdit, QPushButton, QLabel

class Folder(QWidget):
    def __init__(self, name):
        super().__init__()
        self.setFixedSize(200, 200)
        
        layout = QVBoxLayout()
        self.setLayout(layout)

        self.icon = QLabel("📁")  
        self.label = QLabel(name)

        layout.addWidget(self.icon)
        layout.addWidget(self.label)
