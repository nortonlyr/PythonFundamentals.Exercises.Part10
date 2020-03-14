cust_data = {}
acc_data = {}
acc_type = ['Checking', 'Savings']

class Person:
	def __init__(self, id, first_name, last_name):
		self.id = id,
		self.first_name = first_name,
		self.last_name = last_name

	def get_id(self):
		return self.id_

	def get_first_name(self):
		return self.first_name

	def get_last_name(self):
		return self.last_name

class Account:
	def __init__(self, acc_number, acc_type, owner, balance = 0):
		self.acc_number = acc_number,
		self.acc_type = acc_type,
		self.owner = owner,
		self.balance = balance

class Bank(Person, Account):
	def __init__(self):
		pass

	def add_customer(self, id, first_name, last_name):
		if id in cust_data:
			print('ID already exists')
		else:
			cust_data[id] = first_name + " " + last_name
			print(f'Welcome {first_name + " " + last_name}, you new account ID is {id}')

	def add_account(self, id, acc_number, type):
		if id in cust_data and type == 'Checking':
			acc_data[id] = {acc_number:type}
			print(f'{cust_data[id]}, your {acc_type[0]} account is created.')
		else:
			id in cust_data and type == 'Savings'
			acc_data[id] = {acc_number:type}
			print(f'{cust_data[id]}, your {acc_type[1]} account is created.')

	def remove_account(self, account):
		pass

	def deposit(self):
		amount = float(input('Please enter the deposit amount:'))
		self.balance += amount
		print(f'Deposit amount: {amount}')

	def withdraw(self):
		amount = float(input('Please enter the withdraw amount:'))
		if self.balance >= amount:
			self.balance -= amount
			print(f'Your withdrawal amount is {amount}')
		else:
			print('Insufficient fund')

	def balance_inquiry(self):
		print(f'Your available balance: {self.balance}')


cust_bank = Bank()
cust_bank.add_customer(1, 'Norton', 'Lee')
cust_bank.add_customer(2, 'Jacky', 'Robinson')
cust_bank.add_account(1, 1000, 'Checking')
cust_bank.add_account(2, 560, 'Savings')


"""
Constraints
When attempting to register a customer, the customer id must be unique.
When attempting to add an account, the user associated with said account 
must already registered as a customer.
When attempting to add an account, the account number must be unique.
"""