from PyQt5.QtWidgets import QWidget, QVBoxLayout

class Ui_editor(QWidget):
    def __init__(self):
        super().__init__()  # WICHTIG: Basisklasse initialisieren!

        layout = QVBoxLayout()
        self.setLayout(layout)