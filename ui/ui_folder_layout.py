from PyQt5.QtWidgets import QWidget, QVBoxLayout, QTextEdit, QPushButton, QGridLayout
from ui import folder_wigit as folder

columns = 4

class Ui_folder_layout(QWidget):
    def __init__(self, ref_ui_manager=""):
        super().__init__()
        self.ref_ui_manager = ref_ui_manager

        # Layout
        layout = QGridLayout()
        self.setLayout(layout)
        self.ref_ui_manager = ref_ui_manager

        # Widgets
        for idx, folder_name in enumerate(self.ref_ui_manager.getFolder()):
            row = idx // columns
            col = idx % columns

            fw = folder.Folder(folder_name)
            layout.addWidget(fw, row, col)

