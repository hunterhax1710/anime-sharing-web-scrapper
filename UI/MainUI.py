from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QLabel, QMainWindow, QMenuBar,
    QPushButton, QScrollArea, QSizePolicy, QStatusBar,
    QWidget)

class Ui_MainWindow(object):
    # setupUi
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(950, 600)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.sidebar = QWidget(self.centralwidget)
        self.sidebar.setObjectName(u"sidebar")
        self.sidebar.setGeometry(QRect(0, 0, 191, 561))
        self.sidebar.setStyleSheet(u"QWidget{\n"
"	background-color: rgb(1, 15, 48);\n"
"}\n"
"\n"
"")
        self.POSTS = QPushButton(self.sidebar)
        self.POSTS.setObjectName(u"POSTS")
        self.POSTS.setGeometry(QRect(20, 30, 151, 51))
        font = QFont()
        font.setPointSize(20)
        font.setBold(True)
        self.POSTS.setFont(font)
        self.POSTS.setStyleSheet(u"QWidget{\n"
"	background-color: rgb(141, 47, 0);\n"
"	color:white;\n"
"}")
        self.SITES = QPushButton(self.sidebar)
        self.SITES.setObjectName(u"SITES")
        self.SITES.setGeometry(QRect(20, 100, 151, 51))
        self.SITES.setFont(font)
        self.SITES.setStyleSheet(u"QWidget{\n"
"	background-color: rgb(141, 47, 0);\n"
"	color:white;\n"
"}")
        self.POSTS_PAGE = QWidget(self.centralwidget)
        self.POSTS_PAGE.setObjectName(u"POSTS_PAGE")
        self.POSTS_PAGE.setGeometry(QRect(190, 0, 761, 561))
        self.POSTS_PAGE.setStyleSheet(u"QWidget{\n"
"	\n"
"	background-color: rgb(172, 172, 172);\n"
"}")
        self.scrollArea = QScrollArea(self.POSTS_PAGE)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setGeometry(QRect(20, 30, 721, 421))
        self.scrollArea.setStyleSheet(u"QWidget{\n"
"	\n"
"	background-color: rgb(255, 255, 255);\n"
"}")
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 719, 419))
        self.label = QLabel(self.scrollAreaWidgetContents)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(270, 140, 161, 131))
        self.label.setFont(font)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.refreshButton = QPushButton(self.POSTS_PAGE)
        self.refreshButton.setObjectName(u"refreshButton")
        self.refreshButton.setGeometry(QRect(550, 480, 151, 51))
        self.refreshButton.setFont(font)
        self.refreshButton.setStyleSheet(u"QWidget{\n"
"	background-color: rgb(141, 47, 0);\n"
"	color:white;\n"
"}")
        self.SITES_PAGE = QWidget(self.centralwidget)
        self.SITES_PAGE.setObjectName(u"SITES_PAGE")
        self.SITES_PAGE.setGeometry(QRect(190, 0, 761, 561))
        self.SITES_PAGE.setStyleSheet(u"QWidget{\n"
"	\n"
"	background-color: rgb(172, 172, 172);\n"
"}")
        self.scrollArea_3 = QScrollArea(self.SITES_PAGE)
        self.scrollArea_3.setObjectName(u"scrollArea_3")
        self.scrollArea_3.setGeometry(QRect(20, 30, 721, 421))
        self.scrollArea_3.setStyleSheet(u"QWidget{\n"
"	\n"
"	background-color: rgb(255, 255, 255);\n"
"}")
        self.scrollArea_3.setWidgetResizable(True)
        self.scrollAreaWidgetContents_3 = QWidget()
        self.scrollAreaWidgetContents_3.setObjectName(u"scrollAreaWidgetContents_3")
        self.scrollAreaWidgetContents_3.setGeometry(QRect(0, 0, 719, 419))
        self.label_3 = QLabel(self.scrollAreaWidgetContents_3)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(270, 140, 151, 131))
        self.label_3.setFont(font)
        self.scrollArea_3.setWidget(self.scrollAreaWidgetContents_3)
        self.removeButton = QPushButton(self.SITES_PAGE)
        self.removeButton.setObjectName(u"removeButton")
        self.removeButton.setGeometry(QRect(550, 480, 151, 51))
        self.removeButton.setFont(font)
        self.removeButton.setStyleSheet(u"QWidget{\n"
"	background-color: rgb(141, 47, 0);\n"
"	color:white;\n"
"}")
        self.addButton = QPushButton(self.SITES_PAGE)
        self.addButton.setObjectName(u"addButton")
        self.addButton.setGeometry(QRect(60, 480, 151, 51))
        self.addButton.setFont(font)
        self.addButton.setStyleSheet(u"QWidget{\n"
"	background-color: rgb(141, 47, 0);\n"
"	color:white;\n"
"}")
        MainWindow.setCentralWidget(self.centralwidget)
        self.SITES_PAGE.raise_()
        self.POSTS_PAGE.raise_()
        self.sidebar.raise_()
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 950, 22))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.POSTS.clicked.connect(self.POSTS_PAGE.show)
        self.SITES.clicked.connect(self.POSTS_PAGE.hide)
        self.SITES.clicked.connect(self.SITES_PAGE.show)
        self.POSTS.clicked.connect(self.SITES_PAGE.hide)

        QMetaObject.connectSlotsByName(MainWindow)


    # retranslateUi
    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.POSTS.setText(QCoreApplication.translate("MainWindow", u"POSTS", None))
        self.SITES.setText(QCoreApplication.translate("MainWindow", u"SITES", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"POSTS HERE", None))
        self.refreshButton.setText(QCoreApplication.translate("MainWindow", u"Refresh", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"SITES HERE", None))
        self.removeButton.setText(QCoreApplication.translate("MainWindow", u"- Remove", None))
        self.addButton.setText(QCoreApplication.translate("MainWindow", u"+ Add", None))

