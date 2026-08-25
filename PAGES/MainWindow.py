from PySide6.QtWidgets import (QMainWindow, QWidget, QLabel, QVBoxLayout, 
                             QHBoxLayout, QFrame, QMessageBox, QStackedWidget)
from PySide6.QtCore import Qt, QThread, Signal
from PySide6.QtGui import QFont, QCursor, QIcon
from UI.MainUI import Ui_MainWindow
from PAGES.AddWindow import AddWindow
from collections import defaultdict
import config
import scrapper
import os

def clear_layout(layout):
    if layout is not None:
        while layout.count():
            item = layout.takeAt(0)
            widget = item.widget()
            if widget is not None:
                widget.deleteLater()
            else:
                clear_layout(item.layout())

# SITES Page 
class UrlItemWidget(QFrame):
    clicked = Signal(str)  # Emits site_id
    
    def __init__(self, site_id, url, parent=None):
        super().__init__(parent)
        self.setObjectName("UrlItemWidget")
        self.site_id = site_id
        self.url = url
        self.selected = False
        
        self.setFrameShape(QFrame.Shape.StyledPanel)
        self.setCursor(Qt.CursorShape.PointingHandCursor)
        
        layout = QHBoxLayout(self)
        layout.setContentsMargins(10, 5, 10, 5)
        
        self.label = QLabel(url)
        self.label.setFont(QFont("Segoe UI", 10))
        self.label.setWordWrap(True)
        layout.addWidget(self.label)
        
        self.update_style()
        
    def update_style(self):
        if self.selected:
            self.setStyleSheet("""
                #UrlItemWidget {
                    background-color: rgba(141, 47, 0, 30);
                    border: 2px solid rgb(141, 47, 0);
                    border-radius: 4px;
                }
                QLabel {
                    color: rgb(141, 47, 0);
                    font-weight: bold;
                    background: transparent;
                }
            """)
        else:
            self.setStyleSheet("""
                #UrlItemWidget {
                    background-color: #f9f9f9;
                    border: 1px solid #999999;
                    border-radius: 4px;
                }
                #UrlItemWidget:hover {
                    background-color: #eaeaea;
                }
                QLabel {
                    color: #333333;
                    background: transparent;
                }
            """)
            
    def mousePressEvent(self, event):
        if event.button() == Qt.MouseButton.LeftButton:
            self.clicked.emit(self.site_id)


class GroupWidget(QFrame):
    def __init__(self, group_name, urls_data, on_url_clicked, parent=None):
        super().__init__(parent)
        self.setObjectName("GroupWidget")
        self.setFrameShape(QFrame.Shape.StyledPanel)
        self.setStyleSheet("""
            #GroupWidget {
                background-color: #ffffff;
                border: 2px solid #666666;
                border-radius: 6px;
            }
        """)
        
        layout = QHBoxLayout(self)
        layout.setContentsMargins(10, 10, 10, 10)
        layout.setSpacing(15)
        
        # Left side Group label (acting as merged group cell)
        self.group_label = QLabel(group_name)
        group_font = QFont("Segoe UI", 11)
        group_font.setBold(True)
        self.group_label.setFont(group_font)
        self.group_label.setStyleSheet("color: rgb(1, 15, 48); border: none; background: transparent;")
        self.group_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.group_label.setFixedWidth(150)
        self.group_label.setWordWrap(True)
        layout.addWidget(self.group_label)
        
        # Vertical divider line 
        self.separator = QFrame()
        self.separator.setFrameShape(QFrame.Shape.VLine)
        self.separator.setStyleSheet("background-color: #666666; max-width: 1px; border: none;")
        layout.addWidget(self.separator)
        
        # Right side vertical stack of URLs
        self.urls_layout = QVBoxLayout()
        self.urls_layout.setSpacing(6)
        self.urls_layout.setContentsMargins(0, 0, 0, 0)
        
        self.url_widgets = []
        for site_id, url in urls_data:
            url_widget = UrlItemWidget(site_id, url)
            url_widget.clicked.connect(on_url_clicked)
            self.urls_layout.addWidget(url_widget)
            self.url_widgets.append(url_widget)
            
        layout.addLayout(self.urls_layout)


# POSTS Page 
class PostRowWidget(QFrame):
    def __init__(self, group_name, title, url, parent=None):
        super().__init__(parent)
        self.setObjectName("PostRowWidget")
        self.setFrameShape(QFrame.Shape.StyledPanel)
        self.setStyleSheet("""
            #PostRowWidget {
                background-color: #ffffff;
                border-bottom: 2px solid #888888;
            }
            #PostRowWidget:hover {
                background-color: #f5f8ff;
            }
        """)
        
        layout = QHBoxLayout(self)
        layout.setContentsMargins(15, 10, 15, 10)
        layout.setSpacing(15)
        
        # Left side Group name
        self.group_label = QLabel(group_name)
        group_font = QFont("Segoe UI", 10)
        group_font.setBold(True)
        self.group_label.setFont(group_font)
        self.group_label.setStyleSheet("color: #444444; border: none; background: transparent;")
        self.group_label.setFixedWidth(150)
        self.group_label.setWordWrap(True)
        layout.addWidget(self.group_label)
        
        # Vertical divider 
        self.separator = QFrame()
        self.separator.setFrameShape(QFrame.Shape.VLine)
        self.separator.setStyleSheet("background-color: #888888; max-width: 1px; border: none;")
        layout.addWidget(self.separator)
        
        # Right side Clickable Title Link
        self.title_label = QLabel()
        self.title_label.setFont(QFont("Segoe UI", 10))
        self.title_label.setStyleSheet("border: none; background: transparent;")
        link_html = f'<a href="{url}" style="color: #1a73e8; text-decoration: none; font-weight: 500;">{title}</a>'
        self.title_label.setText(link_html)
        self.title_label.setOpenExternalLinks(True)
        self.title_label.setWordWrap(True)
        layout.addWidget(self.title_label)


class HeaderRowWidget(QFrame):
    def __init__(self, col1_text, col2_text, parent=None):
        super().__init__(parent)
        self.setStyleSheet("""
            HeaderRowWidget {
                background-color: rgb(1, 15, 48);
                border-top-left-radius: 4px;
                border-top-right-radius: 4px;
            }
            QLabel {
                color: #ffffff;
                font-weight: bold;
                background: transparent;
            }
        """)
        
        layout = QHBoxLayout(self)
        layout.setContentsMargins(15, 8, 15, 8)
        layout.setSpacing(15)
        
        self.label1 = QLabel(col1_text)
        font1 = QFont("Segoe UI", 10)
        font1.setBold(True)
        self.label1.setFont(font1)
        self.label1.setFixedWidth(150)
        self.label1.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(self.label1)
        
        self.separator = QFrame()
        self.separator.setFrameShape(QFrame.Shape.VLine)
        self.separator.setStyleSheet("background-color: rgba(255, 255, 255, 0.2); max-width: 1px; border: none;")
        layout.addWidget(self.separator)
        
        self.label2 = QLabel(col2_text)
        font2 = QFont("Segoe UI", 10)
        font2.setBold(True)
        self.label2.setFont(font2)
        layout.addWidget(self.label2)


# Background Worker Thread
class ScrapingWorker(QThread):
    finished = Signal(list)
    error = Signal(str)
    
    def run(self):
        try:
            sites = config.load_sites()
            all_posts = []
            for site_id, site in sites.items():
                group = site["group"]
                url = site["url"]
                try:
                    posts = scrapper.scrape(url)
                    for post in posts:
                        all_posts.append({
                            "group": group,
                            "title": post["title"],
                            "url": post["url"]
                        })
                except Exception as e:
                    # Log scraping errors per site and continue
                    print(f"Error scraping site {url}: {e}")
            self.finished.emit(all_posts)
        except Exception as e:
            self.error.emit(str(e))


# MainUI Window Controller
class MainUI(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle("Scrapy")
        
        # Set Window Icon
        icon_path = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "AppIcon.png")
        if os.path.exists(icon_path):
            self.setWindowIcon(QIcon(icon_path))
            
        # State
        self.selected_site_id = None
        self.all_url_widgets = []
        
        # Hide original placeholder text labels
        self.label.hide()
        self.label_3.hide()
        

        # Dynamic Resizing function
        # Main Layout on Central Widget (combine Sidebar and Main Content pages)
        self.main_layout = QHBoxLayout(self.centralwidget)
        self.main_layout.setContentsMargins(0, 0, 0, 0)
        self.main_layout.setSpacing(0)
        
        # Configure Sidebar
        self.sidebar.setFixedWidth(190)
        sidebar_layout = QVBoxLayout(self.sidebar)
        sidebar_layout.setContentsMargins(20, 30, 20, 30)
        sidebar_layout.setSpacing(20)
        self.POSTS.setFixedHeight(51)
        self.SITES.setFixedHeight(51)
        sidebar_layout.addWidget(self.POSTS)
        sidebar_layout.addWidget(self.SITES)
        sidebar_layout.addStretch()
        

        # QStackedWidget to manage the right-side pages
        self.stacked_widget = QStackedWidget(self.centralwidget)
        self.stacked_widget.addWidget(self.POSTS_PAGE)
        self.stacked_widget.addWidget(self.SITES_PAGE)
        
        # Add components to the main layout
        self.main_layout.addWidget(self.sidebar)
        self.main_layout.addWidget(self.stacked_widget)
        

        # Layout for POSTS_PAGE
        posts_page_layout = QVBoxLayout(self.POSTS_PAGE)
        posts_page_layout.setContentsMargins(20, 20, 20, 20)
        posts_page_layout.setSpacing(10)
        
        # Create and add posts header
        self.posts_header = HeaderRowWidget("Website", "Title", self.POSTS_PAGE)
        self.posts_header.setFixedHeight(35)
        posts_page_layout.addWidget(self.posts_header)
        
        # Add scrollArea to layout (resize dynamically)
        posts_page_layout.addWidget(self.scrollArea)
        
        # Bottom row with refreshButton
        bottom_posts_layout = QHBoxLayout()
        bottom_posts_layout.addStretch()
        self.refreshButton.setFixedSize(151, 51)
        bottom_posts_layout.addWidget(self.refreshButton)
        posts_page_layout.addLayout(bottom_posts_layout)
        

        # Layout for SITES_PAGE
        sites_page_layout = QVBoxLayout(self.SITES_PAGE)
        sites_page_layout.setContentsMargins(20, 20, 20, 20)
        sites_page_layout.setSpacing(10)
        
        # Create and add sites header
        self.sites_header = HeaderRowWidget("Group", "URLS", self.SITES_PAGE)
        self.sites_header.setFixedHeight(35)
        sites_page_layout.addWidget(self.sites_header)
        
        # Add scrollArea_3 to layout (resize dynamically)
        sites_page_layout.addWidget(self.scrollArea_3)
        
        # Bottom row with buttons (addButton left, removeButton right)
        bottom_sites_layout = QHBoxLayout()
        self.addButton.setFixedSize(151, 51)
        bottom_sites_layout.addWidget(self.addButton)
        bottom_sites_layout.addStretch()
        self.removeButton.setFixedSize(151, 51)
        bottom_sites_layout.addWidget(self.removeButton)
        sites_page_layout.addLayout(bottom_sites_layout)
        
        # Initialize Layouts for Scroll Areas contents
        self.posts_layout = QVBoxLayout(self.scrollAreaWidgetContents)
        self.posts_layout.setContentsMargins(0, 0, 0, 0)
        self.posts_layout.setSpacing(0)
        self.posts_layout.setAlignment(Qt.AlignmentFlag.AlignTop)
        
        self.sites_layout = QVBoxLayout(self.scrollAreaWidgetContents_3)
        self.sites_layout.setContentsMargins(5, 5, 5, 5)
        self.sites_layout.setSpacing(10)
        self.sites_layout.setAlignment(Qt.AlignmentFlag.AlignTop)
        
        # Disconnect auto-generated signals from setupUi to avoid show/hide conflicts
        try:
            self.POSTS.clicked.disconnect()
        except RuntimeError:
            pass
        try:
            self.SITES.clicked.disconnect()
        except RuntimeError:
            pass
        
        # Connect buttons to stacked widget page switches
        self.POSTS.clicked.connect(lambda: self.stacked_widget.setCurrentWidget(self.POSTS_PAGE))
        self.SITES.clicked.connect(lambda: self.stacked_widget.setCurrentWidget(self.SITES_PAGE))
        
        # Default to showing POSTS_PAGE
        self.stacked_widget.setCurrentWidget(self.POSTS_PAGE)
        
        # Connect Buttons
        self.addButton.clicked.connect(self.open_add_window)
        self.removeButton.clicked.connect(self.remove_selected_site)
        self.removeButton.setEnabled(False)  # Disabled until a URL is selected
        self.refreshButton.clicked.connect(self.start_scraping)
        
        # Initial Welcome Message on Posts Page
        self.show_initial_posts_msg()
        
        # Load sites on SITES page
        self.load_sites_ui()
        
    def open_add_window(self):
        # Open AddWindow modal dialog
        self.add_dialog = AddWindow(self, on_success=self.load_sites_ui)
        self.add_dialog.exec()
        
    def load_sites_ui(self):
        # Reset selection
        self.selected_site_id = None
        self.removeButton.setEnabled(False)
        self.all_url_widgets = []
        
        # Clear layout
        clear_layout(self.sites_layout)
        
        try:
            sites = config.load_sites()
        except Exception as e:
            QMessageBox.critical(self, "Error", f"Failed to load sites: {e}")
            return
            
        if not sites:
            no_sites_label = QLabel("No sites added yet. Click '+ Add' below to add websites to scrape.")
            italic_font = QFont("Segoe UI", 10)
            italic_font.setItalic(True)
            no_sites_label.setFont(italic_font)
            no_sites_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
            no_sites_label.setStyleSheet("color: #777777; margin: 20px;")
            self.sites_layout.addWidget(no_sites_label)
            return
            
        # Group sites by group name
        grouped = defaultdict(list)
        for site_id, site in sites.items():
            grouped[site["group"]].append((site_id, site["url"]))
            
        # Populate layout with GroupWidgets
        for group_name, urls_data in grouped.items():
            group_widget = GroupWidget(group_name, urls_data, self.handle_url_clicked)
            self.sites_layout.addWidget(group_widget)
            self.all_url_widgets.extend(group_widget.url_widgets)
            
    def handle_url_clicked(self, site_id):
        self.selected_site_id = site_id
        self.removeButton.setEnabled(True)
        
        # Update styling of all URL widgets to reflect selection
        for widget in self.all_url_widgets:
            widget.selected = (widget.site_id == site_id)
            widget.update_style()
            
    def remove_selected_site(self):
        if not self.selected_site_id:
            return
            
        reply = QMessageBox.question(
            self, "Confirm Delete", 
            "Are you sure you want to remove this website URL from the scraping configuration?",
            QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No, QMessageBox.StandardButton.No
        )
        
        if reply == QMessageBox.StandardButton.Yes:
            try:
                config.remove_site(self.selected_site_id)
                self.load_sites_ui()
            except Exception as e:
                QMessageBox.critical(self, "Error", f"Failed to remove site: {e}")

    def show_initial_posts_msg(self):
        clear_layout(self.posts_layout)
        welcome_label = QLabel("Click the 'Refresh' button below to start scraping.")
        italic_font = QFont("Segoe UI", 11)
        italic_font.setItalic(True)
        welcome_label.setFont(italic_font)
        welcome_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        welcome_label.setStyleSheet("color: #666666; margin-top: 40px;")
        self.posts_layout.addWidget(welcome_label)

    def start_scraping(self):
        # Clear layout and show loading status
        clear_layout(self.posts_layout)
        self.refreshButton.setEnabled(False)
        self.refreshButton.setText("Scraping...")
        
        loading_label = QLabel("Scraping latest posts... Please wait...")
        italic_font = QFont("Segoe UI", 11)
        italic_font.setItalic(True)
        loading_label.setFont(italic_font)
        loading_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        loading_label.setStyleSheet("color: rgb(141, 47, 0); margin-top: 40px;")
        self.posts_layout.addWidget(loading_label)
        
        # Start Worker Thread
        self.worker = ScrapingWorker(self)
        self.worker.finished.connect(self.handle_scraping_finished)
        self.worker.error.connect(self.handle_scraping_error)
        self.worker.start()
        
    def handle_scraping_finished(self, posts):
        clear_layout(self.posts_layout)
        self.refreshButton.setEnabled(True)
        self.refreshButton.setText("Refresh")
        
        if not posts:
            no_posts_label = QLabel("No posts found. Verify your site configurations or connections.")
            italic_font = QFont("Segoe UI", 11)
            italic_font.setItalic(True)
            no_posts_label.setFont(italic_font)
            no_posts_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
            no_posts_label.setStyleSheet("color: #777777; margin-top: 40px;")
            self.posts_layout.addWidget(no_posts_label)
            return
            
        # Display posts
        for post in posts:
            row_widget = PostRowWidget(post["group"], post["title"], post["url"])
            self.posts_layout.addWidget(row_widget)
            
    def handle_scraping_error(self, err_msg):
        clear_layout(self.posts_layout)
        self.refreshButton.setEnabled(True)
        self.refreshButton.setText("Refresh")
        
        QMessageBox.warning(self, "Scraping Failure", f"An error occurred while loading pages:\n{err_msg}")
        self.show_initial_posts_msg()
        