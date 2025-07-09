from PyQt5.QtWidgets import QWidget, QVBoxLayout, QTextEdit, QPushButton, QLabel

class Folder(QWidget):
    def __init__(self, name="No Name"):
        super().__init__()
        self.setFixedSize(400, 400)
        self.setStyleSheet("""
            background-color: #f0f0f0;
            border: 2px solid black;
            border-radius: 8px;
        """)

        layout = QVBoxLayout()
        self.setLayout(layout)

        self.label = QLabel(name)
        self.label.setStyleSheet("""color: red;font-size: 14px;background-color: #333;""")

        layout.addWidget(self.label)
