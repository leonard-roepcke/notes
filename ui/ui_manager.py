from PyQt5.QtWidgets import QMainWindow, QStackedWidget
from ui import ui_folder_layout
from ui import ui_editor
import file_manager as fm

class UIManager(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Notizen")

        self.stack = QStackedWidget()
        self.setCentralWidget(self.stack)
        self.file_manager = fm.File_manager() # self

        self.folder_layout = ui_folder_layout.Ui_folder_layout(self)
        self.editor_layout = ui_editor.Ui_editor()

        self.stack.addWidget(self.folder_layout)
        self.stack.addWidget(self.editor_layout)

        self.stack.setCurrentWidget(self.folder_layout)

        

    def switch_to_folder_layout(self):
        self.stack.setCurrentWidget(self.folder_layout)

    def switch_to_editor_layout(self):
        self.stack.setCurrentWidget(self.editor_layout)
    
    def getFolder(self):
        print("get Folder:   ",self.file_manager.show_files())
        return self.file_manager.show_files()
    
    def reqest_creat_dir(self):
        self.file_manager.mk_dir("New File: "+str(len(self.file_manager.show_files())))
