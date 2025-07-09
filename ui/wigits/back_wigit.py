from PyQt5.QtWidgets import QWidget, QVBoxLayout, QTextEdit, QPushButton, QLabel

class Back(QWidget):
    def __init__(self):
        super().__init__()
        self.setFixedSize(400, 50)
        self.setStyleSheet("""
            background-color: #f0f0f0;
            border: 2px solid black;
            border-radius: 8px;
        """)

        layout = QVBoxLayout()
        self.setLayout(layout)

        self.label = QLabel("back /..")
        self.label.setStyleSheet("""color: #fff;font-size: 20px;background-color: #333;""")

        layout.addWidget(self.label)
