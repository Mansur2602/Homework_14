import sys
import os
import requests
import json
from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton


class Main(QWidget):
    def __init__(self):
        super().__init__()
        self.init_main()

    def init_main(self):
        self.setWindowTitle("Сохранение файла json")
        self.setGeometry(100, 100, 400, 300)

        layout = QVBoxLayout()

        self.label = QLabel("Введите ID:")
        layout.addWidget(self.label)

        self.entry = QLineEdit()
        layout.addWidget(self.entry)

        self.fetch_button = QPushButton("Получить данные")
        self.fetch_button.clicked.connect(self.fetch_data)
        layout.addWidget(self.fetch_button)

        self.setLayout(layout)

    def fetch_data(self):
        item_id = self.entry.text()

        url = f"https://jsonplaceholder.typicode.com/posts/{item_id}"

        
        response = requests.get(url)
        data = response.json()
        self.save_data(data)
        

    def save_data(self, data):
        folder_name = "json_data"
        if not os.path.exists(folder_name):
            os.makedirs(folder_name)

        file_name = f"{data['id']}.json"
        file_path = os.path.join(folder_name, file_name)

        with open(file_path, 'w') as json_file:
            json.dump(data, json_file, indent=4)



app = QApplication(sys.argv)
window = Main()
window.show()
sys.exit(app.exec())