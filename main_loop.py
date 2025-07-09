import input_handler as inp
from ui import ui_manager as ui
import sys
from PyQt5.QtWidgets import QApplication

app = QApplication(sys.argv)
window = ui.UIManager()
window.showMaximized()
sys.exit(app.exec_())


show_ui = True
def mainloop():
    if show_ui:
        ui.Ui()
    else:
        while True:
            inp.input_handler()