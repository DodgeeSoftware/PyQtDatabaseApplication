# (c) Dodgee Software 2018
# Author Shem Taylor

# Imports
import sys
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtCore import QObject, pyqtSignal

# My Application includes
from DatabaseWrapper import DatabaseWrapper
from MainWindow import MainWindow

# Entry Point of our Application
if __name__ == "__main__":
	
	# Grab the instance of the Database Wrapper
	databaseWrapper = DatabaseWrapper.getInstance()
	
	# Connect to the Database
	if databaseWrapper.connect("127.0.0.1", "admin", "admin") == False:
		sys.exit()
	
	# NOTE: Design Choice I could have made an Application class and file
	# 	and used QApplication as a base class here. This would have the
	#   effect of a tidier main file, I chose not to do this 
	app = QtWidgets.QApplication(sys.argv)
	mainWin = MainWindow()
	mainWin.show()
	sys.exit( app.exec_() )
