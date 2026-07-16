from PySide6.QtWidgets import QDialog, QMessageBox
from UI.AddUI import Ui_AddWindow
import config

class AddWindow(QDialog, Ui_AddWindow):
    def __init__(self, parent=None, on_success=None):
        super().__init__(parent)
        self.setupUi(self)
        self.setWindowTitle("Add Website")
        self.on_success = on_success
        
        # Text Colour
        self.GroupTextEdit.setStyleSheet("background-color: white; color: black;")
        self.URLTextEdit.setStyleSheet("background-color: white; color: black;")
        
        # Connect buttons
        self.confirmButton.clicked.connect(self.handle_confirm)
        self.cancelButton.clicked.connect(self.close)
        
    def handle_confirm(self):
        group = self.GroupTextEdit.toPlainText().strip()
        url = self.URLTextEdit.toPlainText().strip()
        
        if not group or not url:
            QMessageBox.warning(self, "Validation Error", "Both Group and URL fields are required.")
            return
            
        try:
            config.add_site(group, url)
            if self.on_success:
                self.on_success()
            self.accept()  # Close the modal dialog
        except Exception as e:
            QMessageBox.critical(self, "Error", f"Failed to save site: {e}")
