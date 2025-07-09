from PyQt5.QtWidgets import QWidget, QVBoxLayout, QPushButton
from PyQt5.QtWidgets import QSizePolicy

class Add_dir(QWidget):
    def __init__(self, ref_layout=""):
        super().__init__()
        self.setFixedSize(400, 200)
        self.ref_layout = ref_layout

        layout = QVBoxLayout()
        self.setLayout(layout)

        self.button = QPushButton("+ dir")
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
            self.ref_layout.reqest_creat_dir()
