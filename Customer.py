# (c) Dodgee Software 2018
# Author Shem Taylor

# Imports
import sys
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtCore import QObject, pyqtSignal

# Customer Window Class
class Customer:
	
	# ****************
	# * CONSTRUCTORS *
	# ****************
	
	# Constructor which calls base class
	def __init__(self):
		pass
	
	# ***********
	# * MEMBERS *
	# ***********
	customerID = 0
	title = ""
	givenNames = ""
	lastName = ""
