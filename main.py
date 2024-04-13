import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QGridLayout, QPushButton, QMessageBox, QLabel
from PyQt5.QtGui import QFont
from PyQt5.QtCore import Qt

from note_window import NoteWindow
from review_dialog import ReviewDialog
from settings_dialog import SettingsDialog
import config
import database

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('英语学习记录')
        self.setGeometry(100, 100, 400, 300)

        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        layout = QVBoxLayout()
        central_widget.setLayout(layout)

        title_label = QLabel('英语学习记录')
        title_label.setFont(QFont(config.FONT_FAMILY, config.FONT_SIZE + 4))
        title_label.setAlignment(Qt.AlignCenter)
        layout.addWidget(title_label)

        button_layout = QGridLayout()
        layout.addLayout(button_layout)

        note_button = QPushButton('记笔记')
        note_button.setFont(QFont(config.FONT_FAMILY, config.FONT_SIZE))
        note_button.clicked.connect(self.show_note_window)
        button_layout.addWidget(note_button, 0, 0)

        review_button = QPushButton('复习')
        review_button.setFont(QFont(config.FONT_FAMILY, config.FONT_SIZE))
        review_button.clicked.connect(self.show_review_dialog)
        button_layout.addWidget(review_button, 0, 1)

        settings_button = QPushButton('设置')
        settings_button.setFont(QFont(config.FONT_FAMILY, config.FONT_SIZE))
        settings_button.clicked.connect(self.show_settings_dialog)
        button_layout.addWidget(settings_button, 1, 0)

        about_button = QPushButton('关于作者')
        about_button.setFont(QFont(config.FONT_FAMILY, config.FONT_SIZE))
        about_button.clicked.connect(self.show_about_dialog)
        button_layout.addWidget(about_button, 1, 1)

        delete_button = QPushButton('删除笔记')
        delete_button.setFont(QFont(config.FONT_FAMILY, config.FONT_SIZE))
        delete_button.clicked.connect(lambda: ReviewDialog(self, delete_mode=True).exec_())
        button_layout.addWidget(delete_button, 2, 0)


    def show_note_window(self):
        note_window = NoteWindow(self)
        note_window.exec_()

    def show_review_dialog(self):
        review_dialog = ReviewDialog(self)
        review_dialog.exec_()

    def show_settings_dialog(self):
        settings_dialog = SettingsDialog(self)
        if settings_dialog.exec_() == SettingsDialog.Accepted:
            self.update_settings()

    def update_settings(self):
        self.setStyleSheet(f'background-color: {config.BACKGROUND_COLOR}; background-image: url({config.BACKGROUND_IMAGE});')
        font = QFont(config.FONT_FAMILY, config.FONT_SIZE)
        for widget in self.findChildren(QPushButton):
            widget.setFont(font)

    def show_about_dialog(self):
        text = """
            <div>本项目由武汉纺织大学20级学生所作,仅供学习。</div>
            <a href="https://blog.csdn.net/CH2102?spm=1000.2115.3001.5343">关于作者&copy;电气专业——少吃方便面</a>  
        """
        QMessageBox.about(self, "关于作者", text)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    database.create_tables()
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
