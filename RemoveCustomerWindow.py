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

# Remove Customer Window Class
class RemoveCustomerWindow(QMainWindow):

	# *******************
	# * GUI CCOMPONENTS *
	# ******************
	
	__centralWidget = None
	__gridLayout = None
	__idLabel = None
	__idTextBox = None
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
		self.setWindowTitle("Remove Customer")
		
		# Setup Our Central Widget
		self.__centralWidget = QWidget()
		self.__centralWidget.setLayout(QGridLayout())
		self.setCentralWidget(self.__centralWidget)

		# Title Label
		self.__idLabel = QLabel()
		self.__idLabel.setText("ID:")
		self.__centralWidget.layout().addWidget(self.__idLabel, 0, 0)
		
		# ID TextBox
		self.__idTextBox = QLineEdit()
		self.__centralWidget.layout().addWidget(self.__idTextBox, 0, 1)
		
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
		self.__idTextBox.setText("")
	
	# *********
	# * SLOTS *
	# *********
	
	# Ok Button
	def okButtonPushed(self):
		databaseWrapper = DatabaseWrapper.getInstance()
		customerID = int(self.__idTextBox.text())
		databaseWrapper.removeCustomer(customerID)
		self.clear()
		self.close()
		
	# Cancel Button
	def cancelButtonPushed(self):
		self.clear()
		self.close()
