# (c) Dodgee Software 2018
# Author Shem Taylor

# Python Imports
import sys
# MySQLConnector Imports
import mysql.connector
from mysql.connector import errorcode
# My Application Imports
from Customer import Customer

# Database Wrapper Class
class DatabaseWrapper:

	# ****************
	# * CONSTRUCTORS *
	# ****************
	
	# Constructor
	def __init__(self):
		if DatabaseWrapper.__instance != None:
			raise Exception("Tried to Construct DatabaseWrapper more than once. This class is a singleton!")
		else:
			DatabaseWrapper.__instance = self
	
	# *************
	# * SINGLETON *
	# *************
	
	# GetInstance Method
	def getInstance():
		if DatabaseWrapper.__instance == None:
			DatabaseWrapper.__instance = DatabaseWrapper()
		return DatabaseWrapper.__instance
	getInstance = staticmethod(getInstance)
	
	__instance = None
	
	# ***********
	# * GENERAL *
	# ***********
	
	# Connect to the Database
	def connect(self, url, username, password):
		try:
			self.__connection = mysql.connector.connect(user='admin', password='admin', host='127.0.0.1', database='dbtest', auth_plugin='mysql_native_password')
			self.__connection.autocommit = True
		except mysql.connector.Error as err:
			if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
				print("Bad Username or Password")
				return False
			elif err.errno == errorcode.ER_BAD_DB_ERROR:
				print("The Database you want to connect to doesn't exist")
				return False
			else:
				print(err)
				return False
		return True
		
	# Close the Database
	def close():
		if self.__connection != None:
			self.__connection.close()
		
	__connection = None;
	
	# ***********
	# * QUERIES *
	# ***********
	
	# Add Customer
	def addCustomer(self, title, givenNames, lastName):
		if self.__connection == None:
			return False
		if len(title) == 0:
			return False
		if len(givenNames) == 0:
			return False
		if len(lastName) == 0:
			return False
		cursor = self.__connection.cursor()
		query = ('INSERT INTO Customers(Title, GivenNames, LastName) VALUES(\'' + title + '\', \'' + givenNames + '\', \'' + lastName + '\')')
		print(query)
		cursor.execute(query)
		return True
		
	# Is Customer
	def isCustomer(self, customerID):
		if customerID < 0:
			return False
		if self.__connection == None:
			return False
		cursor = self.__connection.cursor()
		query = ('SELECT CustomerID FROM Customers WHERE CustomerID=' + str(customerID))
		print(query)
		cursor.execute(query, (customerID))
		result = cursor.fetchall()
		if cursor.rowcount == 1:
			return True
		return False
		
	# Get Customer
	def getCustomer(self, customerID):
		if customerID < 0:
			return False
		if self.__connection == None:
			return False
		cursor = self.__connection.cursor(dictionary=True)
		query = ('SELECT * FROM Customers WHERE CustomerID=' + str(customerID))
		print(query)
		customer = Customer()
		cursor.execute(query, (customerID))
		result = cursor.fetchall()
		if cursor.rowcount == 1:
			customer.customerID = result[0]['CustomerID']
			customer.title = result[0]['Title']
			customer.givenNames = result[0]['GivenNames']
			customer.lastName = result[0]['LastName']
		return customer
		
	# Get Customers
	def getCustomers(self):
		if self.__connection == None:
			return False
		customers = []
		cursor = self.__connection.cursor(dictionary=True)
		query = ('SELECT * FROM Customers')
		print(query)
		cursor.execute(query)
		result = cursor.fetchall()
		for row in result:
			customer = Customer()
			customer.customerID = row['CustomerID']
			customer.title = row['Title']
			customer.givenNames = row['GivenNames']
			customer.lastName = row['LastName']
			customers.append(customer)
		return customers
		
	# Remove Customer
	def removeCustomer(self, customerID):
		if customerID < 0:
			return False
		if self.__connection == None:
			return False
		cursor = self.__connection.cursor()
		query = ('DELETE FROM Customers WHERE CustomerID=' + str(customerID))
		print(query)
		cursor.execute(query, (customerID))
		self.__connection.commit()
