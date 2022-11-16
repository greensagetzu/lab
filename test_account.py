from account import *

class Test:
	def setup_method(self):
		self.p1 = Account('Jane')
		self.p2 = Account('John')

	def teardown_method(self):
		del self.p1
		del self.p2

	def test__init(self):
		assert self.p1.get_name() == 'Jane'
		assert self.p1.get_balance() == 0
		assert self.p2.get_name() == 'John'
		assert self.p2.get_balance() == 0

		assert self.p1.__str__() == 'account_name = Jane and account_balance = 0'
		assert self.p2.__str__() == 'account_name = John and account_balance = 0'

	def test_deposit(self):
		assert self.p1.deposit(500) == True
		assert self.p1.get_balance()  == 500
		assert self.p1.deposit(-50) == False
		assert self.p1.deposit(0) == False
		assert self.p1.deposit(388) == True
		assert self.p1.get_balance()  == 888

	def test_withdraw(self):
		assert self.p1.withdraw(500) == False
		assert self.p1.withdraw(-50) == False
		assert self.p1.withdraw(0) == False
		assert self.p1.get_balance()  == 0

