from typing import Dict
import pickle


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


class PersistenceUnitls:
    def __init__(self):
        pass

    @staticmethod
    def write_pickel(file_path, data):
        with open(file_path, 'wb') as handler:
            pickle.dump(data, handler)

    @staticmethod
    def load_pickle(file_path):
        with open(file_path, 'rb') as handler:
            data = pickle.load(handler)
        return data
