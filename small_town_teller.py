class Person:
	def __init__(self, id_, first_name, last_name):
		self.id_ = id_
		self.first_name = first_name
		self.last_name = last_name

	def unique_id(id):
		for s in id_:


class Account:
	def __init__(self, number, type_, owner, balance):
		self.number = number
		self.type_ = type_
		self.owner = owner
		self.balance = balance


class Bank:
	def __init__(self):
		# self.add_customer = add_customer

		# self.add_account = add_account
		# self.remove_account = remove_account
		# self.deposit = deposit
		# self.withdraw = withdraw
		# self.balance_inquiry = balance_inquiry

	# def of money deposit
	def add_customer(self):
		add_customer.append(id_)
		add_customer.append(first_name)
		add_customer.append(last_name)

	def add_account(self):
		add_account.append(number)
		add_account.append(type_)
		add_account.append(owner)

	def deposit(self):
		amount = float(input('Please enter the deposit amount:'))
		self.balance += amount
		print('Deposit amount:' + amount)

	def withdraw(self):
		amount = float(input('Please enter the withdraw amount:'))
		if self.balance >= amount
			self.balance -= amount
			print('Your withdrwa amount:' + amount)
		else
			print('Insufficient fund')

	def balance_inquiry(self):
		print('Your current balance:' + self.balance)


"""
Constraints

When attempting to register a customer, the customer id must be unique.
When attempting to add an account, the user associated with said account 
must already registered as a customer.
When attempting to add an account, the account number must be unique.