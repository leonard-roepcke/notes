from PyQt5.QtWidgets import QWidget, QVBoxLayout, QTextEdit, QPushButton

class Ui_editor(QWidget):
    def __init__(self, ref_ui_manager):
        super().__init__()
        self.ref_ui_manager = ref_ui_manager
        self.file_name = ""
        self.file_data = ""

        layout = QVBoxLayout()
        self.setLayout(layout)

        # Das mehrzeilige Textfeld
        self.text_edit = QTextEdit()
        layout.addWidget(self.text_edit)

        # Beispiel-Button zum Speichern
        self.save_button = QPushButton("Speichern")
        self.save_button.clicked.connect(self.save_data)
        layout.addWidget(self.save_button)

        # Initialer Inhalt
        self.update_content(self.file_data)

    def update_content(self, new_data):
        """Setzt file_data und aktualisiert das Textfeld"""
        self.file_data = new_data
        self.text_edit.setPlainText(new_data)
    
    def update_show(self):
        self.text_edit.setPlainText(self.file_data)

    def save_data(self):
        """Speichert den aktuellen Inhalt zurück in file_data"""
        self.file_data = self.text_edit.toPlainText()
        self.ref_ui_manager.set_file(self.file_name, self.file_data)
