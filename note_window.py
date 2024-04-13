from PyQt5.QtWidgets import QDialog, QVBoxLayout, QLabel, QTextEdit, QLineEdit, QPushButton, QMessageBox, QComboBox
from PyQt5.QtGui import QFont

import database
import config

class NoteWindow(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle('记笔记')
        self.setGeometry(100, 100, 400, 300)

        self.layout = QVBoxLayout()
        self.setLayout(self.layout)

        self.content_label = QLabel('英文内容:')
        self.content_label.setFont(QFont(config.FONT_FAMILY, config.FONT_SIZE))
        self.content_edit = QTextEdit()
        self.content_edit.setFont(QFont(config.FONT_FAMILY, config.FONT_SIZE))

        self.content_en_label = QLabel('中文内容:')
        self.content_en_label.setFont(QFont(config.FONT_FAMILY, config.FONT_SIZE))
        self.content_en_edit = QTextEdit()
        self.content_en_edit.setFont(QFont(config.FONT_FAMILY, config.FONT_SIZE))

        self.note_type_label = QLabel('笔记类型:')
        self.note_type_label.setFont(QFont(config.FONT_FAMILY, config.FONT_SIZE))
        self.note_type_combo = QComboBox()
        self.note_type_combo.setFont(QFont(config.FONT_FAMILY, config.FONT_SIZE))
        self.note_type_combo.addItems(['句子', '短语', '单词', '文章'])

        self.note_name_label = QLabel('笔记名称:')
        self.note_name_label.setFont(QFont(config.FONT_FAMILY, config.FONT_SIZE))
        self.note_name_edit = QLineEdit()
        self.note_name_edit.setFont(QFont(config.FONT_FAMILY, config.FONT_SIZE))

        self.save_button = QPushButton('保存')
        self.save_button.setFont(QFont(config.FONT_FAMILY, config.FONT_SIZE))
        self.save_button.clicked.connect(self.save_record)

        self.layout.addWidget(self.content_label)
        self.layout.addWidget(self.content_edit)
        self.layout.addWidget(self.content_en_label)
        self.layout.addWidget(self.content_en_edit)
        self.layout.addWidget(self.note_type_label)
        self.layout.addWidget(self.note_type_combo)
        self.layout.addWidget(self.note_name_label)
        self.layout.addWidget(self.note_name_edit)
        self.layout.addWidget(self.save_button)

    def save_record(self):
        content = self.content_edit.toPlainText()
        content_en = self.content_en_edit.toPlainText()
        note_type = self.note_type_combo.currentText()
        note_name = self.note_name_edit.text()

        if not content or not content_en or not note_name:
            QMessageBox.warning(self, '警告', '请输入内容和笔记名称')
            return

        database.insert_record(note_type, note_name, content, content_en)

        self.content_edit.clear()
        self.content_en_edit.clear()
        self.note_name_edit.clear()

        QMessageBox.information(self, '提示', '记录已保存')