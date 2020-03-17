class Person:
	def __init__(self, id, first_name, last_name):
		self.id = id
		self.first_name = first_name
		self.last_name = last_name

class Account:
	def __init__(self, number, type, owner, balance = 0):
		self.number = number
		self.type = type
		self.owner = owner
		self.balance = balance

class Bank:
	cust_data = []
	acc_data = {}
	acc_type = ['Checking', 'Savings']

	def add_customer(self, customer):
		if customer.id in self.cust_data:
			print('ID already exists')
		else:
			self.cust_data.append(customer.id)

	def add_account(self, account):
		if account not in self.acc_data:
			self.acc_data[account.number] = account.balance

	def remove_account(self, account):
		if account in self.acc_data:
			del[self.acc_data[account]]

	def deposit(self, account, amount):
		self.acc_data[account] += amount


	def withdraw(self, account, amount):
		if self.acc_data[account] >= amount:
			self.acc_data[account] -= amount
		else:
			print('Insufficient fund')

	def balance_inquiry(self, account):
		print(f'Your available balance: {self.acc_data[account]}')


cust_bank = Bank()
Norton = Person(10101, 'Norton', 'Lee')

cust_bank.add_customer(Norton)
print(cust_bank.cust_data)


Norton_Checking = Account(7000, 'Checking', Norton)
print(cust_bank.acc_data)

cust_bank.add_account(Norton_Checking)
print(cust_bank.acc_data)

cust_bank.deposit(7000, 10000)
print(cust_bank.acc_data)

cust_bank.withdraw(7000, 4000)
print(cust_bank.acc_data)

cust_bank.balance_inquiry(7000)


"""
Constraints
When attempting to register a customer, the customer id must be unique.
When attempting to add an account, the user associated with said account 
must already registered as a customer.
When attempting to add an account, the account number must be unique.
"""