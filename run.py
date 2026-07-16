import sys
from PySide6.QtWidgets import QApplication
from Pages.MainWindow import MainUI

app = QApplication(sys.argv)

window = MainUI()
window.show()
app.exec()