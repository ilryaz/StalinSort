import sys
from PySide6.QtWidgets import (QApplication, QMainWindow, QWidget,
                               QVBoxLayout, QHBoxLayout, QPushButton,
                               QListWidget, QComboBox, QListWidgetItem,
                               QLabel, QDialog, QLineEdit)

class AddDialog(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Add item")

        layout = QVBoxLayout(self)

        self.input_field = QLineEdit()
        self.input_field.setPlaceholderText("Enter title")

        self.add_button = QPushButton("Add")
        self.add_button.clicked.connect(self.accept)

        layout.addWidget(QLabel("Title:"))
        layout.addWidget(self.input_field)
        layout.addWidget(self.add_button)

        self.setFixedSize(200, 100)

    def get_text(self):
        return self.input_field.text()

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('StalinSort 3000')
        self.setup_ui()
    
    def setup_ui(self):
        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        # layouts
        main_layout = QVBoxLayout(central_widget)
        lower_layout = QHBoxLayout()

        # the list containing files
        self.file_list = QListWidget()
        self.file_list.addItem(QListWidgetItem('1'))
        self.file_list.addItem(QListWidgetItem('2'))
        self.file_list.addItem(QListWidgetItem('5'))
        self.file_list.addItem(QListWidgetItem('3'))

        # buttons (later add 1-2 sec text change on press; sort changes to sorting -> sorted)
        self.load_file_button_text = "Load file"
        self.load_file_button = QPushButton(self.load_file_button_text)

        self.add_button_text = "Add"
        self.add_button = QPushButton(self.add_button_text)
        self.add_button.clicked.connect(self.add_button_clicked)

        self.sort_button_text = "Sort"
        self.sort_button = QPushButton(self.sort_button_text)

        self.save_button_text = "Save"
        self.save_button = QPushButton(self.save_button_text)

        main_layout.addWidget(self.file_list)
        lower_layout.addWidget(self.load_file_button)
        lower_layout.addWidget(self.add_button)
        lower_layout.addWidget(self.sort_button)
        lower_layout.addWidget(self.save_button)
        main_layout.addLayout(lower_layout)

    def add_button_clicked(self):
        dialog = AddDialog()

        if dialog.exec():
            text = dialog.get_text()
            if text:
                self.file_list.addItem(QListWidgetItem(text))
    
    def get_list_content(self, somelist):
        content = []
        for i in range(somelist.count()):
            item = somelist.item(i)
            content.append(item.text())
        return content

    def stalin_sort(self, data):
        new_data = []
        main_type = type(data[0])

        for datum in data:
            if not new_data:
                new_data.append(datum)

            elif type(datum) == main_type:
                if datum >= new_data[-1]:
                    new_data.append(datum)

        return new_data

app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec()