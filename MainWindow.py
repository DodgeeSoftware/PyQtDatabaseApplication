# (c) Dodgee Software 2018
# Author Shem Taylor

# Imports
import sys
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtCore import QObject, pyqtSignal

# My Application Imports
from AddNewCustomerWindow import AddNewCustomerWindow
from Customer import Customer
from CustomerWindow import CustomerWindow
from FindCustomerWindow import FindCustomerWindow
from RemoveCustomerWindow import RemoveCustomerWindow
from ShowCustomersWindow import ShowCustomersWindow
import Application

# Main Window Class
class MainWindow(QMainWindow):

	# *******************
	# * GUI CCOMPONENTS *
	# *******************
	
	__centralWidget = None
	__addCustomerButton = None
	__findCustomerButton = None
	__removeCustomerButton = None
	__showCustomersButton = None

	# ***********
	# * WINDOWS *
	# ***********
	
	__addNewCustomerWindow = None
	__findCustomerWindow = None
	__removeCustomerWindow = None
	__showCustomersWindow = None
	
	# ****************
	# * CONSTRUCTORS *
	# ****************
	
	# Constructor
	def __init__(self):
		QMainWindow.__init__(self)
		
		# Set the Minimum Size of the Window
		self.setMinimumSize(QSize(312, 77))		
		# Set the Window Title
		self.setWindowTitle("Main Window") 
		
		# Setup Our Central Widget
		self.__centralWidget = QWidget()
		self.__centralWidget.setLayout(QGridLayout())
		self.setCentralWidget(self.__centralWidget)
		
		# Add Customer Button
		self.__addCustomerButton = QPushButton()
		self.__addCustomerButton.setText("Add Customer")
		self.__addCustomerButton.clicked.connect(self.addCustomerButtonPushed)
		self.__centralWidget.layout().addWidget(self.__addCustomerButton, 1, 0)
		
		# Find Customer Button
		self.__findCustomerButton = QPushButton()
		self.__findCustomerButton.setText("Find Customer")
		self.__findCustomerButton.clicked.connect(self.findCustomerButtonPushed)
		self.__centralWidget.layout().addWidget(self.__findCustomerButton, 1, 1)

		# Remove Customer Button
		self.__removeCustomerButton = QPushButton()
		self.__removeCustomerButton.setText("Remove Customer")
		self.__removeCustomerButton.clicked.connect(self.removeCustomerButtonPushed)
		self.__centralWidget.layout().addWidget(self.__removeCustomerButton, 2, 0)

		# Show Customers Button
		self.__showCustomersButton = QPushButton()
		self.__showCustomersButton.setText("Show Customers")
		self.__showCustomersButton.clicked.connect(self.showCustomersButtonPushed)
		self.__centralWidget.layout().addWidget(self.__showCustomersButton, 2, 1)

		# Quit Button
		self.__quitButton = QPushButton()
		self.__quitButton.setText("Quit")
		self.__quitButton.clicked.connect(self.quitButtonPushed)
		self.__centralWidget.layout().addWidget(self.__quitButton, 3, 0)
		
		# About Button
		self.__aboutButton = QPushButton()
		self.__aboutButton.setText("About")
		self.__aboutButton.clicked.connect(self.aboutButtonPushed)
		self.__centralWidget.layout().addWidget(self.__aboutButton, 3, 1)
		
		# Windows
		self.__addNewCustomerWindow = AddNewCustomerWindow()
		self.__findCustomerWindow = FindCustomerWindow()
		self.__removeCustomerWindow = RemoveCustomerWindow()
		self.__showCustomersWindow = ShowCustomersWindow()
		
	# *********
	# * SLOTS *
	# *********
	
	# Pushed Add Customer Button
	def addCustomerButtonPushed(self):
		print("addCustomerButtonPushed")
		self.__addNewCustomerWindow = AddNewCustomerWindow()
		self.__addNewCustomerWindow.clear()
		self.__addNewCustomerWindow.show()
	
	# Pushed Find Customer Button
	def findCustomerButtonPushed(self):
		print("findCustomerButtonPushed")
		self.__findCustomerWindow = FindCustomerWindow()
		self.__findCustomerWindow.clear()
		self.__findCustomerWindow.show()
	
	# Pushed Remove Customer Button
	def removeCustomerButtonPushed(self):
		print("removeCustomerButtonPushed")
		self.__removeCustomerWindow = RemoveCustomerWindow()
		self.__removeCustomerWindow.show()
	
	# Pushed Show Customer Button
	def showCustomersButtonPushed(self):
		print("showCustomersButtonPushed")
		self.__showCustomersWindow = ShowCustomersWindow()
		self.__showCustomersWindow.clear()
		self.__showCustomersWindow.refresh()
		self.__showCustomersWindow.show()
	
	# Quit Button
	def quitButtonPushed(self):
		print('quitButtonPushed')
		self.close()
	
	# Pushed About Button
	def aboutButtonPushed(self):
		aboutMessageBox = QMessageBox()
		aboutMessageBox.setWindowTitle("About")
		aboutMessageBox.setText("(c) Dodgee Software 2018")
		aboutMessageBox.exec()
