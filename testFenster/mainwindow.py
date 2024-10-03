import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QPushButton, QWidget, QStackedWidget, QGridLayout, QTextEdit

# Define the Notes Module
class NotesModule(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setStyleSheet("background-color: white; color: black;")  # Set background to white and text color to black
        layout = QVBoxLayout()

        # Button and Text Field
        button = QPushButton("This is the Notes Module")
        button.setStyleSheet("color: black;")  # Set text color to black
        layout.addWidget(button)

        # Add a text field for notes
        text_field = QTextEdit()
        text_field.setPlaceholderText("Enter notes here...")
        layout.addWidget(text_field)

        layout.addStretch()  # Ensure it takes full height
        self.setLayout(layout)

# Define the Calendar Module
class CalendarModule(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setStyleSheet("background-color: white; color: black;")  # Set background to white and text color to black
        layout = QVBoxLayout()

        # Button and Text Field
        button = QPushButton("This is the Calendar Module")
        button.setStyleSheet("color: black;")  # Set text color to black
        layout.addWidget(button)

        # Add a text field for calendar details
        text_field = QTextEdit()
        text_field.setPlaceholderText("Enter calendar details here...")
        layout.addWidget(text_field)

        layout.addStretch()  # Ensure it takes full height
        self.setLayout(layout)

# Define the To-Do List Module
class TodoModule(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setStyleSheet("background-color: white; color: black;")  # Set background to white and text color to black
        layout = QVBoxLayout()

        # Button and Text Field
        button = QPushButton("This is the To-Do List Module")
        button.setStyleSheet("color: black;")  # Set text color to black
        layout.addWidget(button)

        # Add a text field for to-do list
        text_field = QTextEdit()
        text_field.setPlaceholderText("Enter your to-do items here...")
        layout.addWidget(text_field)

        layout.addStretch()  # Ensure it takes full height
        self.setLayout(layout)

# Define the Wissenarchiv Module
class WissenarchivModule(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setStyleSheet("background-color: white; color: black;")  # Set background to white and text color to black
        layout = QVBoxLayout()

        # Button and Text Field
        button = QPushButton("This is the Wissenarchiv Module")
        button.setStyleSheet("color: black;")  # Set text color to black
        layout.addWidget(button)

        # Add a text field for Wissenarchiv content
        text_field = QTextEdit()
        text_field.setPlaceholderText("Enter knowledge archive content here...")
        layout.addWidget(text_field)

        layout.addStretch()  # Ensure it takes full height
        self.setLayout(layout)

# Define the Main GUI Loader
class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.setWindowTitle("GUI Loader App")
        self.setGeometry(100, 100, 1024, 768)  # Main window size

        # Create a stacked widget to hold different modules
        self.stacked_widget = QStackedWidget()

        # Add different module instances to the stacked widget
        self.notes_module = NotesModule()
        self.calendar_module = CalendarModule()
        self.todo_module = TodoModule()
        self.wissenarchiv_module = WissenarchivModule()

        self.stacked_widget.addWidget(self.notes_module)
        self.stacked_widget.addWidget(self.calendar_module)
        self.stacked_widget.addWidget(self.todo_module)
        self.stacked_widget.addWidget(self.wissenarchiv_module)

        # Create buttons to switch between modules
        self.button_notes = QPushButton("Notes")
        self.button_calendar = QPushButton("Calendar")
        self.button_todo = QPushButton("To-Do List")
        self.button_wissenarchiv = QPushButton("Wissenarchiv")

        # Connect buttons to the corresponding module
        self.button_notes.clicked.connect(self.show_notes)
        self.button_calendar.clicked.connect(self.show_calendar)
        self.button_todo.clicked.connect(self.show_todo)
        self.button_wissenarchiv.clicked.connect(self.show_wissenarchiv)

        # Create a sidebar layout
        sidebar_layout = QVBoxLayout()
        sidebar_layout.addWidget(self.button_notes)
        sidebar_layout.addWidget(self.button_calendar)
        sidebar_layout.addWidget(self.button_todo)
        sidebar_layout.addWidget(self.button_wissenarchiv)
        sidebar_layout.addStretch()

        sidebar_widget = QWidget()
        sidebar_widget.setLayout(sidebar_layout)

        # Create the main layout using QGridLayout
        main_layout = QGridLayout()

        # Add sidebar to the grid layout (1/5 of the width)
        main_layout.addWidget(sidebar_widget, 0, 0, 1, 1)  # 1/5 vertical, 1/5 horizontal

        # Add the stacked widget (content area) to the grid layout (4/5 of the width)
        main_layout.addWidget(self.stacked_widget, 0, 1, 1, 4)  # 4/5 vertical, 5/5 horizontal

        # Set stretch factors: 1 for sidebar, 4 for main content
        main_layout.setColumnStretch(0, 1)
        main_layout.setColumnStretch(1, 4)

        # Set the central widget with the grid layout
        container_widget = QWidget()
        container_widget.setLayout(main_layout)
        self.setCentralWidget(container_widget)

        # Show the first module by default
        self.show_notes()

    def show_notes(self):
        self.stacked_widget.setCurrentWidget(self.notes_module)

    def show_calendar(self):
        self.stacked_widget.setCurrentWidget(self.calendar_module)

    def show_todo(self):
        self.stacked_widget.setCurrentWidget(self.todo_module)

    def show_wissenarchiv(self):
        self.stacked_widget.setCurrentWidget(self.wissenarchiv_module)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())