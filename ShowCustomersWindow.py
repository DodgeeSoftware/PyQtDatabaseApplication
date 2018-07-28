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

# Show Customers Window Class
class ShowCustomersWindow(QMainWindow):
	
	# *******************
	# * GUI CCOMPONENTS *
	# *******************
	
	__centralWidget = None
	__customerTableWidget = None
	
	# ****************
	# * CONSTRUCTORS *
	# ****************
	
	# Constructor which calls base class
	def __init__(self):
		QMainWindow.__init__(self)

		# Set the Minimum Size of the Window
		self.setMinimumSize(QSize(312, 77))
		
		# Set the Window Title
		self.setWindowTitle("Show Customers") 
		
		# Setup Our Central Widget
		self.__centralWidget = QWidget()
		self.__centralWidget.setLayout(QGridLayout())
		self.setCentralWidget(self.__centralWidget)
		
		# Add the Table to the Window
		self.__customerTableWidget = QTableWidget(self)
		self.__customerTableWidget.setColumnCount(4)
		self.__customerTableWidget.setRowCount(20)
		self.__customerTableWidget.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeMode.Stretch)
		self.__customerTableWidget.horizontalHeader().hide()
		self.__customerTableWidget.verticalHeader().setVisible(False)
		self.__customerTableWidget.setEditTriggers(QAbstractItemView.NoEditTriggers)
		self.__centralWidget.layout().addWidget(self.__customerTableWidget)
	
	# ***********
	# * GENERAL *
	# ***********
	
	# Refresh the Window
	def refresh(self):
		print("refresh")
		databaseWrapper = DatabaseWrapper.getInstance()
		customers = databaseWrapper.getCustomers()
		self.__customerTableWidget.setColumnCount(4)
		self.__customerTableWidget.setRowCount(len(customers))
		i = 0;
		for customer in customers:
			self.__customerTableWidget.setItem(i, 0, QTableWidgetItem(str(customer.customerID)))
			self.__customerTableWidget.setItem(i, 1, QTableWidgetItem(str(customer.title)))
			self.__customerTableWidget.setItem(i, 2, QTableWidgetItem(str(customer.givenNames)))
			self.__customerTableWidget.setItem(i, 3, QTableWidgetItem(str(customer.lastName)))
			i = i + 1
		self.__customerTableWidget.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeMode.Stretch)
		self.__customerTableWidget.horizontalHeader().hide()
		self.__customerTableWidget.verticalHeader().setVisible(False)
		self.__customerTableWidget.setEditTriggers(QAbstractItemView.NoEditTriggers)
	
	# Clear the Window
	def clear(self):
		self.__customerTableWidget.clearSpans()