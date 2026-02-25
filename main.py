import sys
from PySide6.QtWidgets import (QApplication, QMainWindow, QWidget,
                               QVBoxLayout, QHBoxLayout, QPushButton,
                               QListWidget, QComboBox, QListWidgetItem,
                               QLabel)

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
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


app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec()