# (c) Dodgee Software 2018
# Author Shem Taylor

# Imports
import sys
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtCore import QObject, pyqtSignal

# My Application Imports
from DatabaseWrapper import DatabaseWrapper

# Customer Window Class
class CustomerWindow(QMainWindow):

	# *******************
	# * GUI CCOMPONENTS *
	# ******************
	
	__centralWidget = None
	__gridLayout = None
	__titleLabel = None
	__idTextBox = None
	__titleComboBox = None
	__givenNamesLabel = None
	__givenNamesTextBox = None
	__lastNameLabel = None
	__lastNameTextBox = None
	__okButton = None
	
	# ****************
	# * CONSTRUCTORS *
	# ****************
	
	# Constructor which calls base class
	def __init__(self):
		QMainWindow.__init__(self)
		
		# Set the Minimum Size of the Window
		self.setMinimumSize(QSize(312, 77))
		
		# Set the Window Title
		self.setWindowTitle("Customer")
		
		# Setup Our Central Widget
		self.__centralWidget = QWidget()
		self.__centralWidget.setLayout(QGridLayout())
		self.setCentralWidget(self.__centralWidget)

		# Title Label
		self.__idLabel = QLabel(self)
		self.__idLabel.setText("ID:")
		self.__centralWidget.layout().addWidget(self.__idLabel, 0, 0)
		
		# Title ComboBox
		self.__titleComboBox = QComboBox(self)
		self.__titleComboBox.addItem("Mr")
		self.__titleComboBox.addItem("Mrs")
		self.__titleComboBox.addItem("Ms")
		self.__titleComboBox.setEditable(False)
		self.__centralWidget.layout().addWidget(self.__titleComboBox, 0, 1)
		
		# ID TextBox
		self.__idTextBox = QLineEdit(self)
		self.__centralWidget.layout().addWidget(self.__idTextBox, 0, 1)
		
		# Given-Names Label
		self.__givenNamesLabel = QLabel(self)
		self.__givenNamesLabel.setText("Given-Names")
		self.__centralWidget.layout().addWidget(self.__givenNamesLabel, 1, 0)
		
		# Given Names TextBox
		self.__givenNamesTextBox = QLineEdit(self)
		self.__givenNamesTextBox.setReadOnly(True)
		self.__centralWidget.layout().addWidget(self.__givenNamesTextBox, 1, 1)

		# Last Name Label
		self.__lastNameLabel = QLabel(self)
		self.__lastNameLabel.setText("Given-Names")
		self.__centralWidget.layout().addWidget(self.__lastNameLabel, 2, 0)
		
		# Last Name TextBox
		self.__lastNameTextBox = QLineEdit(self)
		self.__lastNameTextBox.setReadOnly(True)
		self.__centralWidget.layout().addWidget(self.__lastNameTextBox, 2, 1)
		
		# Ok Button
		self.__okButton = QPushButton(self)
		self.__okButton.setText("Ok")
		self.__okButton.clicked.connect(self.okButtonPushed)
		self.__centralWidget.layout().addWidget(self.__okButton, 3, 0)
		
	# ***********
	# * GENERAL *
	# ***********
	
	# Clear the Window
	def clear(self):
		self.__idTextBox.setText('')
		#self.__titleComboBox.setCurrentText('')
		self.__givenNamesTextBox.setText('')
		self.__lastNameTextBox.setText('')
		pass
	
	# Set the Customer
	def setCustomer(self, customer):
		self.__idTextBox.setText(str(customer.customerID))
		self.__titleComboBox.setCurrentText(customer.title)
		self.__givenNamesTextBox.setText(customer.givenNames)
		self.__lastNameTextBox.setText(customer.lastName)
		pass
		
	# *********
	# * SLOTS *
	# *********

	# Ok Button
	def okButtonPushed(self):
		self.clear()
		self.close()