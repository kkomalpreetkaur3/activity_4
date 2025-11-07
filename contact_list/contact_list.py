"""The module defines the ContactList class."""

__author__ = "Komalpreet Kaur"
__version__ = "1.0.0"
__credits__ = ""

from PySide6.QtWidgets import  QMainWindow, QLineEdit, QPushButton, QTableWidget, QLabel, QVBoxLayout, QWidget, QTableWidgetItem, QMessageBox
from PySide6.QtCore import Slot, Qt
class ContactList(QMainWindow):
    """Represents a window that provides the UI to manage contacts."""

    def __init__(self):
        """Initializes a new instance of the ContactList class."""
        super().__init__()
        self.__contacts = [] 
        self.__initialize_widgets()  
        self.__connect_signals()

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

    def __connect_signals(self):
        """Connect signals to their respective slots."""
        self.add_button.clicked.connect(self.__on_add_contact)
        self.remove_button.clicked.connect(self.__on_remove_contact)
        self.contact_table.cellClicked.connect(self.__on_select_contact)

    @Slot()
    def __on_add_contact(self):
        """Slot to add a contact to the list and table."""
        name = self.contact_name_input.text().strip()
        phone = self.phone_input.text().strip()

        if not name or not phone:
            self.status_label.setText("Please enter a contact name and phone number.")
            return
        
        # Add to internal list
        self.__contacts.append((name, phone))

        # Add to table
        row = self.contact_table.rowCount()
        self.contact_table.insertRow(row)

        self.contact_table.setItem(row, 0, QTableWidgetItem(name))

        phone_item = QTableWidgetItem(phone)
        phone_item.setTextAlignment(Qt.AlignRight | Qt.AlignVCenter)
        self.contact_table.setItem(row, 1, phone_item)

        self.status_label.setText(f"Added contact: {name}")

        self.contact_name_input.clear()
        self.phone_input.clear()
        self.contact_name_input.setFocus()

    @Slot()
    def __on_remove_contact(self):
        """Slot to remove the selected contact from the list and table."""
        row = self.contact_table.currentRow()
        if row == -1:
            self.status_label.setText("Please select a row to be removed.")
            return
        
        # retrieve name for popup
        name_item = self.contact_table.item(row, 0)
        contact_name = name_item.text() if name_item else "this contact"
        
        # QMessageBox CONFIRMATION
        reply = QMessageBox.question(
            self,
            "Remove Contact",
            "Are you sure you want to remove the selected contact?",
            QMessageBox.Yes | QMessageBox.No,
            QMessageBox.No
        )

        if reply == QMessageBox.Yes:
            self.__contacts.pop(row)
            self.contact_table.removeRow(row)
            self.status_label.setText("Contact removed.")
        else:
            self.status_label.setText("Contact not removed.")

    @Slot(int, int)
    def __on_select_contact(self, row: int, column: int):
        """Slot to handle selecting a contact in the table."""
        name_item = self.contact_table.item(row, 0)
        phone_item = self.contact_table.item(row, 1)

        if name_item and phone_item:
            self.contact_name_input.setText(name_item.text())
            self.phone_input.setText(phone_item.text())
            self.status_label.setText(f"Selected contact: {name_item.text()}")
