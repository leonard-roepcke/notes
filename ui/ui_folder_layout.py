from PyQt5.QtWidgets import QWidget, QVBoxLayout, QTextEdit, QPushButton, QGridLayout, QScrollArea
from ui.wigits import folder_wigit as folder
from ui.wigits import back_wigit as back , add_dir_wigit as add_dir, add_file_wigit as add_file, add_projekt_wigit as add_projekt

columns = 4

class Ui_folder_layout(QWidget):
    def __init__(self, ref_ui_manager=""):
        super().__init__()
        self.ref_ui_manager = ref_ui_manager

        # Layout
        main_layout = QGridLayout()
        self.setLayout(main_layout)
        
        scroll = QScrollArea()
        scroll.setWidgetResizable(True)  # Wichtig!
        main_layout.addWidget(scroll)

        content_widget = QWidget()
        grid_layout = QGridLayout()
        content_widget.setLayout(grid_layout)

        scroll.setWidget(content_widget)

        # Widgets
        grid_layout.addWidget(back.Back(), 0, 0)
        grid_layout.addWidget(add_file.Add_file(), 0, 1)
        grid_layout.addWidget(add_dir.Add_dir(), 0, 2)
        grid_layout.addWidget(add_projekt.Add_projekt(), 0, 3)

        for idx, folder_name in enumerate(self.ref_ui_manager.getFolder()):
            row = idx // columns
            col = idx % columns

            fw = folder.Folder(folder_name)
            grid_layout.addWidget(fw, row+1, col)

