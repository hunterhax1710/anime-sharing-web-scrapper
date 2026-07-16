import sys
import os
from PySide6.QtWidgets import QApplication
from PySide6.QtGui import QIcon
from PAGES.MainWindow import MainUI

app = QApplication(sys.argv)

# Application Icon
icon_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "AppIcon.png")
if os.path.exists(icon_path):
    app.setWindowIcon(QIcon(icon_path))

window = MainUI()
window.show()
app.exec()