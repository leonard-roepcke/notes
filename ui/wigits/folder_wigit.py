from PyQt5.QtWidgets import QWidget, QVBoxLayout, QTextEdit, QPushButton, QLabel
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QSizePolicy

class Folder(QWidget):
    def __init__(self,ref_layout="" , name="No Name"):
        super().__init__()
        self.name = name
        self.ref_layout = ref_layout
        self.setFixedSize(400, 200)
        self.setStyleSheet("""
            background-color: #f0f0f0;
            border: 2px solid black;
            border-radius: 8px;
        """)

        layout = QVBoxLayout()
        self.setLayout(layout)

        self.button = QPushButton(self.name)
        self.button.setStyleSheet("""
            color: #fff;
            font-size: 20px;
            background-color: #333;
            border: 2px solid black;
            border-radius: 8px;
        """)
        self.button.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)

        layout.addWidget(self.button)

        # Hier verbindest du das Klicksignal mit deiner Funktion
        self.button.clicked.connect(self.on_click)

    def on_click(self):
            self.ref_layout.reqest_cd_dir(self.name)