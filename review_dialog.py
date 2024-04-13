from PyQt5.QtWidgets import QDialog, QVBoxLayout, QTableWidget, QTableWidgetItem, QHeaderView, QMessageBox, QAbstractItemView, QPushButton
from PyQt5.QtGui import QFont
from PyQt5.QtCore import Qt

import database
from note_preview import NotePreviewDialog
import config

class ReviewDialog(QDialog):
    def __init__(self, parent=None, delete_mode=False):
        super().__init__(parent)

        self.setWindowTitle('复习' if not delete_mode else '删除笔记')
        self.setGeometry(100, 100, 600, 400)

        self.layout = QVBoxLayout()
        self.setLayout(self.layout)

        self.table = QTableWidget()
        self.table.setFont(QFont(config.FONT_FAMILY, config.FONT_SIZE))
        self.table.setColumnCount(4)
        self.table.setHorizontalHeaderLabels(['ID', '记录时间', '笔记类型', '笔记名称'])
        self.table.setEditTriggers(QTableWidget.NoEditTriggers)
        self.table.cellDoubleClicked.connect(self.show_note_preview)
        if delete_mode:
            self.table.setSelectionMode(QAbstractItemView.ExtendedSelection)
            self.table.setSelectionBehavior(QAbstractItemView.SelectRows)
        else:
            self.table.setSelectionMode(QAbstractItemView.SingleSelection)
            self.table.setSelectionBehavior(QAbstractItemView.SelectRows)

        self.layout.addWidget(self.table)

        if delete_mode:
            delete_button = QPushButton('删除选中笔记')
            delete_button.setFont(QFont(config.FONT_FAMILY, config.FONT_SIZE))
            delete_button.clicked.connect(self.delete_selected_records)
            self.layout.addWidget(delete_button)

        self.populate_table()

    def populate_table(self):
        records = database.get_all_records()

        if not records:
            QMessageBox.information(self, '复习', '没有找到记录')
            return

        self.table.setRowCount(len(records))

        for i, record in enumerate(records):
            for j, value in enumerate(record):
                item = QTableWidgetItem(str(value))
                self.table.setItem(i, j, item)

        self.table.resizeColumnsToContents()
        self.table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)

    def show_note_preview(self, row, column):
        record_id = int(self.table.item(row, 0).text())
        content, content_en = database.get_record_by_id(record_id)

        preview_dialog = NotePreviewDialog(content, content_en)
        preview_dialog.exec_()

    def delete_selected_records(self):
        selected_rows = self.table.selectionModel().selectedRows()
        if not selected_rows:
            return

        confirm = QMessageBox.question(self, '删除笔记', '确定要删除选中的笔记吗？', QMessageBox.Yes | QMessageBox.No)
        if confirm == QMessageBox.Yes:
            for row in reversed(sorted(row.row() for row in selected_rows)):
                record_id = int(self.table.item(row, 0).text())
                database.delete_record(record_id)
                self.table.removeRow(row)

            QMessageBox.information(self, '删除笔记', '笔记已删除')
