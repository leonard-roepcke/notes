from PyQt5.QtWidgets import QWidget, QVBoxLayout, QTextEdit, QPushButton

class Ui_folder_layout(QWidget):
    def __init__(self):
        super().__init__()

        # Layout
        layout = QVBoxLayout()
        self.setLayout(layout)

        # Widgets
        self.text_edit = QTextEdit()
        self.save_button = QPushButton("Speichern")

        layout.addWidget(self.text_edit)
        layout.addWidget(self.save_button)

        # Logik (nur Beispiel)
        self.save_button.clicked.connect(self.save_note)

    def save_note(self):
        text = self.text_edit.toPlainText()
        print("Notiz gespeichert:", text)