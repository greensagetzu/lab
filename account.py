
class Account:
	def __init__(self, name):
		self.__name = name
		self.__balance = 0

	def get_balance(self):
		return self.__balance

	def deposit(self, amount):
		if amount < 0 or amount == 0:
			return False
		else:
			self.__balance += amount
			return True

	def withdraw(self, amount):
		if amount < 0 or amount == 0:
			return False
		elif amount > self.__balance:
			return False
		else:
			self.__balance -= amount
			return True

	def get_name(self):
		return self.__name

	def __str__(self):
		return f'account_name = {self.__name} and account_balance = {self.__balance}'


def main():
	account_one = Account('001-John')
	
	account_one.deposit(100)
	account_one.deposit(200)
	account_one.withdraw(400)
	account_one.withdraw(50)

	print(account_one)

	name = input('Enter the name: ')
	account_two = Account(name)

	deposit_num = int(input('Enter amount to be desposited: '))
	account_two.deposit(deposit_num)
	print(account_two)

	withdraw_num = int(input('Enter amount to be withdrawn: '))
	account_two.withdraw(withdraw_num)
	print(account_two)


if __name__ == '__main__':
	main()