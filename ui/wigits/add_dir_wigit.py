from PyQt5.QtWidgets import QWidget, QVBoxLayout, QPushButton
from PyQt5.QtWidgets import QSizePolicy

class Add_dir(QWidget):
    def __init__(self):
        super().__init__()
        self.setFixedSize(400, 200)

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
        print("Button wurde geklickt!")
        # Hier rufst du deine Funktion aus dem Manager auf
        # z.B. self.ref_manager.add_directory()
