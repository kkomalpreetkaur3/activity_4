"""The module defines the ContactList class."""

__author__ = "Komalpreet Kaur"
__version__ = "1.0.0"
__credits__ = ""

from PySide6.QtWidgets import  QMainWindow, QLineEdit, QPushButton, QTableWidget, QLabel, QVBoxLayout, QWidget, QTableWidgetItem
from PySide6.QtCore import Slot, Qt

self.__contacts = []
class ContactList(QMainWindow):
    """Represents a window that provides the UI to manage contacts."""

    def __init__(self):
        """Initializes a new instance of the ContactList class."""
        super().__init__()
        self.setWindowTitle("Contact List")

        # Input fields
        self.contact_name_input = QLineEdit()
        self.contact_name_input.setPlaceholderText("Contact Name")

        self.phone_input = QLineEdit()
        self.phone_input.setPlaceholderText("Phone Number")

        self.add_button = QPushButton("Add Contact")
        self.remove_button = QPushButton("Remove Contact")
        layout.addWidget(self.add_button)
        layout.addWidget(self.remove_button)

        self.contact_table = QTableWidget()
        self.contact_table.setColumnCount(2)
        self.contact_table.setHorizontalHeaderLabels(["Name", "Phone"])
        layout.addWidget(self.contact_table)

        self.status_label = QLabel()
        layout.addWidget(self.status_label)

        container = QWidget()
        layout = QVBoxLayout()
        layout.addWidget(self.contact_name_input)
        layout.addWidget(self.phone_input)
        container.setLayout(layout)
        self.setCentralWidget(container)
        self.__initialize_widgets()    

        self.add_button.clicked.connect(self.__add_contact)
        self.remove_button.clicked.connect(self.__remove_contact)
        self.contact_table.cellClicked.connect(self.__on_select_contact)  

    def __initialize_widgets(self):
        """Initializes the widgets on this Window.
        
        DO NOT EDIT.
        """
        self.setWindowTitle("Contact List")

        self.contact_name_input = QLineEdit(self)
        self.contact_name_input.setPlaceholderText("Contact Name")

        self.phone_input = QLineEdit(self)
        self.phone_input.setPlaceholderText("Phone Number")

        self.add_button = QPushButton("Add Contact", self)
        self.remove_button = QPushButton("Remove Contact", self)
        
        self.contact_table = QTableWidget(self)
        self.contact_table.setColumnCount(2)
        self.contact_table.setHorizontalHeaderLabels(["Name", "Phone"])

        self.status_label = QLabel(self)

        layout = QVBoxLayout()
        layout.addWidget(self.contact_name_input)
        layout.addWidget(self.phone_input)
        layout.addWidget(self.add_button)
        layout.addWidget(self.remove_button)
        layout.addWidget(self.contact_table)
        layout.addWidget(self.status_label)

        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

@Slot()
def __remove_contact(self):
    row = self.contact_table.currentRow()
    if row == -1:
        self.status_label.setText("Error: No contact selected to remove.")
        return

    removed_contact = self.__contacts.pop(row)
    self.contact_table.removeRow(row)
    self.status_label.setText(f"Removed contact: {removed_contact[0]}")
