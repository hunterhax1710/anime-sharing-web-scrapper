from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QLabel, QPushButton, QSizePolicy,
    QTextEdit, QWidget)

class Ui_AddWindow(object):
    # setupUi
    def setupUi(self, AddWindow):
        if not AddWindow.objectName():
            AddWindow.setObjectName(u"AddWindow")
        AddWindow.resize(421, 250)
        AddWindow.setStyleSheet(u"QWidget{\n"
"	\n"
"	background-color: rgb(172, 172, 172);\n"
"}")
        self.confirmButton = QPushButton(AddWindow)
        self.confirmButton.setObjectName(u"confirmButton")
        self.confirmButton.setGeometry(QRect(30, 180, 131, 41))
        font = QFont()
        font.setPointSize(15)
        font.setBold(True)
        self.confirmButton.setFont(font)
        self.confirmButton.setStyleSheet(u"QWidget{\n"
"	background-color: rgb(141, 47, 0);\n"
"	color:white;\n"
"}")
        self.grouplabel = QLabel(AddWindow)
        self.grouplabel.setObjectName(u"grouplabel")
        self.grouplabel.setGeometry(QRect(10, 30, 71, 51))
        self.grouplabel.setFont(font)
        self.GroupTextEdit = QTextEdit(AddWindow)
        self.GroupTextEdit.setObjectName(u"GroupTextEdit")
        self.GroupTextEdit.setGeometry(QRect(90, 40, 311, 31))
        self.GroupTextEdit.setStyleSheet(u"	\n"
"QWidget{\n"
"	background-color: rgb(255, 255, 255);\n"
"}")
        self.urllabel = QLabel(AddWindow)
        self.urllabel.setObjectName(u"urllabel")
        self.urllabel.setGeometry(QRect(30, 90, 51, 51))
        self.urllabel.setFont(font)
        self.URLTextEdit = QTextEdit(AddWindow)
        self.URLTextEdit.setObjectName(u"URLTextEdit")
        self.URLTextEdit.setGeometry(QRect(90, 100, 311, 31))
        self.URLTextEdit.setStyleSheet(u"	\n"
"QWidget{\n"
"	background-color: rgb(255, 255, 255);\n"
"}")
        self.cancelButton = QPushButton(AddWindow)
        self.cancelButton.setObjectName(u"cancelButton")
        self.cancelButton.setGeometry(QRect(260, 180, 131, 41))
        self.cancelButton.setFont(font)
        self.cancelButton.setStyleSheet(u"QWidget{\n"
"	background-color: rgb(141, 47, 0);\n"
"	color:white;\n"
"}")

        self.retranslateUi(AddWindow)

        QMetaObject.connectSlotsByName(AddWindow)

    # retranslateUi
    def retranslateUi(self, AddWindow):
        AddWindow.setWindowTitle(QCoreApplication.translate("AddWindow", u"Form", None))
        self.confirmButton.setText(QCoreApplication.translate("AddWindow", u"Confirm", None))
        self.grouplabel.setText(QCoreApplication.translate("AddWindow", u"Group:", None))
        self.urllabel.setText(QCoreApplication.translate("AddWindow", u"URL:", None))
        self.cancelButton.setText(QCoreApplication.translate("AddWindow", u"Cancel", None))

