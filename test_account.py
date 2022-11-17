import pytest
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

	def test_deposit(self):
		assert self.p1.deposit(500) == True
		assert self.p1.get_balance()  == 500
		assert self.p1.deposit(-50) == False
		assert self.p1.get_balance()  == 500
		assert self.p1.deposit(0) == False
		assert self.p1.get_balance()  == 500
		assert self.p1.deposit(388.8) == True
		assert self.p1.get_balance()  == pytest.approx(888.8, abs=0.001)

		assert self.p2.deposit(1000) == True
		assert self.p2.get_balance()  == 1000
		assert self.p2.deposit(-500) == False
		assert self.p2.get_balance()  == 1000
		assert self.p2.deposit(0) == False
		assert self.p2.get_balance()  == 1000
		assert self.p2.deposit(555.5) == True
		assert self.p2.get_balance()  == pytest.approx(1555.5, abs=0.001)

	def test_withdraw(self):

		assert self.p1.withdraw(500) == False
		assert self.p1.get_balance()  == 0
		assert self.p1.withdraw(-50) == False
		assert self.p1.get_balance()  == 0
		assert self.p1.withdraw(0) == False
		assert self.p1.get_balance()  == 0

		self.p1.deposit(500) 
		assert self.p1.withdraw(20.5) == True
		assert self.p1.get_balance() == pytest.approx(479.5, abs=0.001)

		assert self.p2.withdraw(250) == False
		assert self.p2.get_balance()  == 0
		assert self.p2.withdraw(-5) == False
		assert self.p2.get_balance()  == 0
		assert self.p2.withdraw(0) == False
		assert self.p2.get_balance()  == 0

		self.p2.deposit(1700) 
		assert self.p2.withdraw(500.25) == True
		assert self.p2.get_balance() == pytest.approx(1199.75, abs=0.001)


		

