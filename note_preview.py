from PyQt5.QtWidgets import QDialog, QVBoxLayout, QLabel, QScrollArea, QWidget, QHBoxLayout
from PyQt5.QtGui import QFont
from PyQt5.QtCore import Qt

import config

class NotePreviewDialog(QDialog):
    def __init__(self, content, content_en):
        super().__init__()

        self.setWindowTitle('笔记预览')
        self.setGeometry(100, 100, 600, 400)

        self.layout = QVBoxLayout()
        self.setLayout(self.layout)

        self.scroll_area = QScrollArea()
        self.scroll_area.setWidgetResizable(True)

        self.content_widget = QWidget()
        self.content_layout = QHBoxLayout()
        self.content_widget.setLayout(self.content_layout)

        self.scroll_area.setWidget(self.content_widget)

        self.content_label = QLabel(content)
        self.content_label.setFont(QFont(config.FONT_FAMILY, config.FONT_SIZE))
        self.content_label.setWordWrap(True)
        self.content_label.setAlignment(Qt.AlignTop)

        self.content_en_label = QLabel(content_en)
        self.content_en_label.setFont(QFont(config.FONT_FAMILY, config.FONT_SIZE))
        self.content_en_label.setWordWrap(True)
        self.content_en_label.setAlignment(Qt.AlignTop)

        self.content_layout.addWidget(self.content_label)
        self.content_layout.addWidget(self.content_en_label)

        self.layout.addWidget(self.scroll_area)
