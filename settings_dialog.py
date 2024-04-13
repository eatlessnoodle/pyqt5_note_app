from PyQt5.QtWidgets import QDialog, QVBoxLayout, QLabel, QLineEdit, QPushButton, QColorDialog, QFileDialog
from PyQt5.QtGui import QFont, QColor

import config

class SettingsDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle('设置')
        self.setGeometry(100, 100, 300, 200)

        layout = QVBoxLayout()
        self.setLayout(layout)

        self.background_color_label = QLabel('背景颜色:')
        self.background_color_label.setFont(QFont(config.FONT_FAMILY, config.FONT_SIZE))
        self.background_color_edit = QLineEdit(config.BACKGROUND_COLOR)
        self.background_color_edit.setFont(QFont(config.FONT_FAMILY, config.FONT_SIZE))
        self.background_color_button = QPushButton('选择颜色')
        self.background_color_button.setFont(QFont(config.FONT_FAMILY, config.FONT_SIZE))
        self.background_color_button.clicked.connect(self.choose_background_color)

        self.background_image_label = QLabel('背景图片:')
        self.background_image_label.setFont(QFont(config.FONT_FAMILY, config.FONT_SIZE))
        self.background_image_edit = QLineEdit(config.BACKGROUND_IMAGE)
        self.background_image_edit.setFont(QFont(config.FONT_FAMILY, config.FONT_SIZE))
        self.background_image_button = QPushButton('选择图片')
        self.background_image_button.setFont(QFont(config.FONT_FAMILY, config.FONT_SIZE))
        self.background_image_button.clicked.connect(self.choose_background_image)

        self.font_family_label = QLabel('字体:')
        self.font_family_label.setFont(QFont(config.FONT_FAMILY, config.FONT_SIZE))
        self.font_family_edit = QLineEdit(config.FONT_FAMILY)
        self.font_family_edit.setFont(QFont(config.FONT_FAMILY, config.FONT_SIZE))

        self.font_size_label = QLabel('字号:')
        self.font_size_label.setFont(QFont(config.FONT_FAMILY, config.FONT_SIZE))
        self.font_size_edit = QLineEdit(str(config.FONT_SIZE))
        self.font_size_edit.setFont(QFont(config.FONT_FAMILY, config.FONT_SIZE))

        self.save_button = QPushButton('保存')
        self.save_button.setFont(QFont(config.FONT_FAMILY, config.FONT_SIZE))
        self.save_button.clicked.connect(self.save_settings)

        layout.addWidget(self.background_color_label)
        layout.addWidget(self.background_color_edit)
        layout.addWidget(self.background_color_button)
        layout.addWidget(self.background_image_label)
        layout.addWidget(self.background_image_edit)
        layout.addWidget(self.background_image_button)
        layout.addWidget(self.font_family_label)
        layout.addWidget(self.font_family_edit)
        layout.addWidget(self.font_size_label)
        layout.addWidget(self.font_size_edit)
        layout.addWidget(self.save_button)

    def choose_background_color(self):
        color = QColorDialog.getColor(QColor(config.BACKGROUND_COLOR), self, '选择背景颜色')
        if color.isValid():
            self.background_color_edit.setText(color.name())

    def choose_background_image(self):
        file_path, _ = QFileDialog.getOpenFileName(self, '选择背景图片', '', 'Image Files (*.png *.jpg *.bmp)')
        if file_path:
            self.background_image_edit.setText(file_path)

    def save_settings(self):
        config.BACKGROUND_COLOR = self.background_color_edit.text()
        config.BACKGROUND_IMAGE = self.background_image_edit.text()
        config.FONT_FAMILY = self.font_family_edit.text()
        config.FONT_SIZE = int(self.font_size_edit.text())
        self.accept()