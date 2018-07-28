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

# Add New Customer Window Class
class AddNewCustomerWindow(QMainWindow):
	
	# *******************
	# * GUI CCOMPONENTS *
	# ******************
	
	__centralWidget = None
	__gridLayout = None
	__titleLabel = None
	__titleComboBox = None
	__givenNamesLabel = None
	__givenNamesTextBox = None
	__lastNameLabel = None
	__lastNameTextBox = None
	__okButton = None
	__cancelButton = None
	
	# ****************
	# * CONSTRUCTORS *
	# ****************
	
	# Constructor which calls base class
	def __init__(self):
		QMainWindow.__init__(self)
		
		# Set the Minimum Size of the Window
		self.setMinimumSize(QSize(312, 77))		
		# Set the Window Title
		self.setWindowTitle("Add New Customer") 
		
		# Setup Our Central Widget
		self.__centralWidget = QWidget()
		self.__centralWidget.setLayout(QGridLayout())
		self.setCentralWidget(self.__centralWidget)
		
		# Title Label
		self.__titleLabel = QLabel()
		self.__titleLabel.setText("Title")
		self.__centralWidget.layout().addWidget(self.__titleLabel, 0, 0)
		
		# Title ComboBox
		self.__titleComboBox = QComboBox()
		self.__titleComboBox.addItem("Mr")
		self.__titleComboBox.addItem("Mrs")
		self.__titleComboBox.addItem("Ms")
		self.__centralWidget.layout().addWidget(self.__titleComboBox, 0, 1)
		
		# Given-Names Label
		self.__givenNamesLabel = QLabel()
		self.__givenNamesLabel.setText("Given-Names")
		self.__centralWidget.layout().addWidget(self.__givenNamesLabel, 1, 0)
		
		# Given Names TextBox
		self.__givenNamesTextBox = QLineEdit()
		self.__centralWidget.layout().addWidget(self.__givenNamesTextBox, 1, 1)
		
		# Last Name Label
		self.__lastNameLabel = QLabel()
		self.__lastNameLabel.setText("Given-Names")
		self.__centralWidget.layout().addWidget(self.__lastNameLabel, 2, 0)
		
		# Last Name TextBox
		self.__lastNameTextBox = QLineEdit()
		self.__centralWidget.layout().addWidget(self.__lastNameTextBox, 2, 1)
		
		# Ok Button
		self.__okButton = QPushButton()
		self.__okButton.setText("Ok")
		self.__okButton.clicked.connect(self.okButtonPushed)
		self.__centralWidget.layout().addWidget(self.__okButton, 3, 0)
		
		# Cancel Button
		self.__cancelButton = QPushButton()
		self.__cancelButton.setText("Cancel")
		self.__cancelButton.clicked.connect(self.cancelButtonPushed)
		self.__centralWidget.layout().addWidget(self.__cancelButton, 3, 1)
	
	# ***********
	# * GENERAL *
	# ***********
	
	# Clear GUI
	def clear(self):
		self.__titleComboBox.setCurrentIndex(0)
		self.__givenNamesTextBox.setText("")
		self.__lastNameTextBox.setText("")
	
	# *********
	# * SLOTS *
	# *********
	
	# Ok Button
	def okButtonPushed(self):
		databaseWrapper = DatabaseWrapper.getInstance()
		title = str(self.__titleComboBox.currentText())
		givenNames = str(self.__givenNamesTextBox.text())
		lastName = str(self.__lastNameTextBox.text())
		databaseWrapper.addCustomer(title, givenNames, lastName)
		self.clear()
		self.close()
		
	# Cancel Button
	def cancelButtonPushed(self):
		self.clear()
		self.close()