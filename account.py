class Account:
	def __init__(self, name):
		self.__account_name = name
		self.__account_balance = 0

	def get_balance(self):
		return self.__account_balance

	def deposit(self, amount):
		if amount < 0 or amount == 0:
			return False
		else:
			self.__account_balance += amount
			return True

	def withdraw(self, amount):
		if amount < 0 or amount == 0:
			return False
		elif amount > self.__account_balance:
			return False
		else:
			self.__account_balance -= amount
			return True

	def get_name(self):
		return self.__account_name

	#def __str__(self):
	 	#return f'account_name = {self.__account_name} and account_balance = {self.__account_balance}'


#checking the code can be run
def main():
	account_one = Account('001-John')
	
	account_one.deposit(1000)
	account_one.deposit(-250)
	account_one.deposit(0)
	account_one.withdraw(400)
	account_one.withdraw(-50)
	account_one.withdraw(0)

	print(account_one)

	name = input('Enter the name: ')
	account_two = Account(name)

	deposit_num = float(input('Enter amount to be desposited: '))
	account_two.deposit(deposit_num)
	print(account_two)

	withdraw_num = float(input('Enter amount to be withdrawn: '))
	account_two.withdraw(withdraw_num)
	print(account_two)


if __name__ == '__main__':
	main()