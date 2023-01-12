import sys
import subprocess
import pkg_resources

required = {'PyQt6', 'openai', 'py-openapi-schema-to-json-schema'}
installed = {pkg.key for pkg in pkg_resources.working_set}
missing = required - installed

if missing:
    python = sys.executable
    subprocess.check_call([python, '-m', 'pip', 'install', *missing], stdout=subprocess.DEVNULL)

import sys

from PyQt6.QtWidgets import QApplication, QMainWindow
from PyQt6.QtCore import pyqtSlot
from PyQt6.uic import loadUi

from gpt import getModelIDs, getCompletion

class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.load_ui()

    def load_ui(self):
        self.ui = loadUi("form.ui",self)
        screen = QApplication.primaryScreen()
        size = screen.size()
        # Positionning
        self.app_width = int(0.9*size.width())
        self.app_height = int(0.9*size.height())

        # Setting same ratio as the screen
        self.setFixedWidth(self.app_width)
        self.setFixedHeight(self.app_height)

        self.x = int(size.width()/2-self.app_width/2)
        self.y = int(size.height()/2-self.app_height/2-30)

        self.setGeometry(self.x, self.y, self.app_width, self.app_height)

        models = getModelIDs()
        models.sort()
        self.combo_models.clear()
        self.combo_models.addItems(models)
        self.combo_models.setCurrentIndex(48)

        # Connect signals and slots
        self.button_send.clicked.connect(self.send_prompt)

    @pyqtSlot()
    def send_prompt(self):
        model = self.combo_models.currentText()
        prompt = self.input.toPlainText()
        response = getCompletion(model, prompt)
        self.output.setText(response)



if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = MainWindow()
    widget.show()
    sys.exit(app.exec())
