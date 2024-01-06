import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QListWidget, QPushButton, QLineEdit, QLabel

class ToDoListApp(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle('Список дел')
        self.setGeometry(100, 100, 400, 300)

        self.tasks_list = QListWidget()
        self.input_task = QLineEdit()
        self.add_button = QPushButton('Добавить')
        self.delete_button = QPushButton('Удалить')
        self.completed_label = QLabel('Выполнено:')

        main_layout = QVBoxLayout()

        input_layout = QHBoxLayout()
        input_layout.addWidget(self.input_task)
        input_layout.addWidget(self.add_button)

        main_layout.addLayout(input_layout)
        main_layout.addWidget(self.tasks_list)
        main_layout.addWidget(self.completed_label)
        main_layout.addWidget(self.delete_button)

        self.setLayout(main_layout)

        self.add_button.clicked.connect(self.add_task)
        self.delete_button.clicked.connect(self.delete_task)
        self.tasks_list.itemClicked.connect(self.task_completed)

    def add_task(self):
        task_text = self.input_task.text()
        if task_text:
            self.tasks_list.addItem(task_text)
            self.input_task.clear()

    def delete_task(self):
        selected_task = self.tasks_list.currentRow()
        if selected_task >= 0:
            self.tasks_list.takeItem(selected_task)

    def task_completed(self):
        completed_tasks = self.tasks_list.selectedItems()
        count = len(completed_tasks)
        self.completed_label.setText(f'Выполнено: {count}')

def main():
    app = QApplication(sys.argv)
    todo_app = ToDoListApp()
    todo_app.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
