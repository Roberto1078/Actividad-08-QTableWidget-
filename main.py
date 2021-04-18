from PySide2.QtWidgets import QApplication
from mainwindow import Mainwindow
import sys

app = QApplication()
window = Mainwindow()
window.show()
sys.exit(app.exec_())